import json
import random
import string
import numpy as np
import re
from random import choice


def generate_one_line(rule_complex, events, field_len, value_len, kwargs: dict):
    rule_complex.write("{\n")
    events.write("{")

    rule_num = 0
    for r in kwargs.values():
        rule_num += r

    out = []

    if "exact" in kwargs.keys() and kwargs["exact"] > 0:
        field_for_rule = ""
        value_for_rule = ""
        for k in range(kwargs["exact"]):
            new_filed = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )
            new_value = "".join(
                random.choice(string.ascii_lowercase) for _ in range(value_len)
            )

            out.append(list([new_filed, new_value]))

            if k == 0:
                field_for_rule = new_filed
                value_for_rule = new_value

            if k < rule_num - 1:
                events.write('"' + new_filed + '":' + '"' + new_value + '",')
            else:
                events.write('"' + new_filed + '":' + '"' + new_value + '"')
        rule_complex.write(
            '    "' + field_for_rule + '": ' + '[ "' + value_for_rule + '" ]\n'
        )
    if "prefix" in kwargs.keys() and kwargs["prefix"] > 0:
        field_for_rule = ""
        value_for_rule = ""
        for i in range(kwargs["prefix"]):
            new_filed = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )

            prefix_len = random.randint(1, value_len)
            no_prefix_len = value_len - prefix_len

            prefix = "".join(
                random.choice(string.ascii_lowercase) for _ in range(prefix_len)
            )
            all_field_with_prefix = prefix + "".join(
                random.choice(string.ascii_lowercase) for _ in range(no_prefix_len)
            )

            out.append(list([new_filed, all_field_with_prefix, "prefix"]))

            if i == 0:
                field_for_rule = new_filed
                value_for_rule = prefix

            if kwargs["exact"] + i < rule_num - 1:
                events.write(
                    '"' + new_filed + '":' + '"' + all_field_with_prefix + '",'
                )
            else:
                events.write('"' + new_filed + '":' + '"' + all_field_with_prefix + '"')
        # else:
        rule_complex.write(
            '    "'
            + field_for_rule
            + '": '
            + '[ {"prefix": "'
            + value_for_rule
            + '" } ]\n'
        )
    if "suffix" in kwargs.keys() and kwargs["suffix"] > 0:
        field_for_rule = ""
        value_for_rule = ""
        for i in range(kwargs["suffix"]):
            new_filed = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )

            prefix_len = random.randint(1, value_len)
            no_prefix_len = value_len - prefix_len

            prefix = "".join(
                random.choice(string.ascii_lowercase) for _ in range(prefix_len)
            )
            all_field_with_prefix = (
                "".join(
                    random.choice(string.ascii_lowercase) for _ in range(no_prefix_len)
                )
                + prefix
            )

            out.append(list([new_filed, all_field_with_prefix, "suffix"]))

            if i == 0:
                field_for_rule = new_filed
                value_for_rule = prefix

            if kwargs["exact"] + +kwargs["prefix"] + i < rule_num - 1:
                events.write(
                    '"' + new_filed + '":' + '"' + all_field_with_prefix + '",'
                )
            else:
                events.write('"' + new_filed + '":' + '"' + all_field_with_prefix + '"')
        rule_complex.write(
            '    "'
            + field_for_rule
            + '": '
            + '[ {"suffix": "'
            + value_for_rule
            + '" } ]\n'
        )

    if "equals-ignore-case" in kwargs.keys() and kwargs["equals-ignore-case"] > 0:
        field_for_rule = ""
        value_for_rule = ""

        for i in range(kwargs["equals-ignore-case"]):
            new_filed = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )
            new_value = "".join(
                random.choice(string.ascii_lowercase) for _ in range(value_len)
            )
            new_value_random_case = "".join(
                choice((str.upper, str.lower))(c) for c in new_value
            )

            out.append(list([new_filed, new_value_random_case, "equals-ignore-case"]))

            if i == 0:
                field_for_rule = new_filed
                value_for_rule = new_value

            if (
                kwargs["exact"] + +kwargs["prefix"] + kwargs["suffix"] + i
                < rule_num - 1
            ):
                events.write(
                    '"' + new_filed + '":' + '"' + new_value_random_case + '",'
                )
            else:
                events.write('"' + new_filed + '":' + '"' + new_value_random_case + '"')
        rule_complex.write(
            '    "'
            + field_for_rule
            + '": '
            + '[ {"equals-ignore-case": "'
            + value_for_rule
            + '" } ]\n'
        )
    if "wildcard" in kwargs.keys() and kwargs["wildcard"] > 0:
        field_for_rule = ""
        value_for_rule = ""

        for i in range(kwargs["wildcard"]):
            new_filed = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )
            len_wildcard = 100
            start_wildcard = random.randint(0, value_len - len_wildcard)

            suitable_for_wildcard = "".join(
                random.choice(string.ascii_lowercase) for _ in range(len_wildcard)
            )

            value_before_wildcard = "".join(
                random.choice(string.ascii_lowercase) for _ in range(start_wildcard)
            )
            value_after_wildcard = "".join(
                random.choice(string.ascii_lowercase)
                for _ in range(value_len - start_wildcard - len_wildcard)
            )

            full_suitable_value = (
                value_before_wildcard + suitable_for_wildcard + value_after_wildcard
            )

            if i == 0:
                field_for_rule = new_filed
                value_for_rule = value_before_wildcard + "*" + value_after_wildcard

            out.append(list([new_filed, full_suitable_value, "wildcard"]))

            if (
                kwargs["exact"]
                + kwargs["prefix"]
                + kwargs["suffix"]
                + kwargs["equals-ignore-case"]
                + i
                < rule_num - 1
            ):
                events.write('"' + new_filed + '":' + '"' + full_suitable_value + '",')
            else:
                events.write('"' + new_filed + '":' + '"' + full_suitable_value + '"')
        rule_complex.write(
            '    "'
            + field_for_rule
            + '": '
            + '[ {"wildcard": "'
            + value_for_rule
            + '" } ]\n'
        )
    if "anything-but" in kwargs.keys() and kwargs["anything-but"] > 0:
        field_for_rule = ""
        value_for_rule = ""

        for i in range(kwargs["anything-but"]):
            new_field = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )
            new_value = "".join(
                random.choice(string.ascii_lowercase) for _ in range(value_len)
            )

            suitable_for_rule = new_value
            while suitable_for_rule == new_value:
                suitable_for_rule = "".join(
                    random.choice(string.ascii_lowercase) for _ in range(value_len)
                )

            if i == 0:
                field_for_rule = new_field
                value_for_rule = suitable_for_rule

            out.append(list([new_field, new_value, "anything-but"]))

            if (
                kwargs["exact"]
                + kwargs["prefix"]
                + kwargs["suffix"]
                + kwargs["equals-ignore-case"]
                + kwargs["wildcard"]
                + i
                < rule_num - 1
            ):
                events.write('"' + new_field + '":' + '"' + new_value + '",')
            else:
                events.write('"' + new_field + '":' + '"' + new_value + '"')
        rule_complex.write(
            '    "'
            + field_for_rule
            + '": '
            + '[ {"anything-but": "'
            + value_for_rule
            + '" } ]\n'
        )
    if "numeric" in kwargs.keys() and kwargs["numeric"] > 0:
        field_for_rule = ""
        low_value_for_rule = ""
        upper_for_rule = ""

        for i in range(kwargs["numeric"]):
            new_field = "".join(
                random.choice(string.ascii_lowercase) for _ in range(field_len)
            )
            low_board = random.uniform(0.0, 1000000.0)
            upper_board = random.uniform(low_board, 1000000.0)

            suitable_value = random.uniform(low_board, upper_board)

            if i == 0:
                field_for_rule = new_field

            if i == 0:
                low_value_for_rule = low_board
                upper_for_rule = upper_board

            out.append(list([new_field, suitable_value, "numeric"]))

            if (
                kwargs["exact"]
                + kwargs["prefix"]
                + kwargs["suffix"]
                + kwargs["equals-ignore-case"]
                + kwargs["wildcard"]
                + kwargs["anything-but"]
                + i
                < rule_num - 1
            ):
                events.write('"' + new_field + '":' + str(suitable_value) + ",")
            else:
                events.write('"' + new_field + '":' + str(suitable_value))
        rule_complex.write(
            '    "'
            + field_for_rule
            + '": '
            + '[ {"numeric": [">",'
            + str(low_value_for_rule)
            + ', "<", '
            + str(upper_for_rule)
            + "] } ]\n"
        )
    rule_complex.write("}")
    events.write("}\n")
    return out


NUMERIC_TYPES = ["numeric"]


def build_event(field: str, value: str, type="exact"):
    if type not in NUMERIC_TYPES:
        return f'"{field}": "{value}"'
    return f'"{field}": {value}'


def generate_from_out(out):
    new = "{"
    for i, pair in enumerate(out):
        if len(pair) == 2:
            new += build_event(pair[0], pair[1])
        else:
            new += build_event(pair[0], pair[1], pair[2])
        if i < len(out) - 1:
            new += ","
    new += "}\n"
    return new


def generate_random_str(str_len):
    return


def change_value(new_pair, pair):
    if len(pair) > 2 and pair[2] == "numeric":
        pair[1] = random.uniform(0.0, 1000000.0)
        return
    l = len(pair[1])
    new_pair[1] = "".join(random.choice(string.ascii_lowercase) for _ in range(l))


def generate(event_num, field_len_max: int, value_len_max, kwargs):
    for field_len in range(1, field_len_max + 1, 5):
        with open(f"rule_{field_len}.json", "w") as rule_complex:
            with open(f"events_{field_len}.json", "w") as events:
                out = generate_one_line(
                    rule_complex=rule_complex,
                    events=events,
                    field_len=field_len,
                    value_len=value_len_max,
                    kwargs=kwargs,
                )

                for _ in range(event_num):
                    copy_out = [[0] * 3 for _ in range(len(out))]
                    value_needs_change = np.random.choice(
                        [0, 1], size=len(out), p=[0.8, 0.2]
                    )

                    for j in range(len(out)):
                        copy_out[j] = list(np.copy(out[j]))
                        if value_needs_change[j] == 1:
                            change_value(copy_out[j], out[j])
                    new = generate_from_out(copy_out)
                    events.write(new)


def add_quotes_to_rule(num):
    with open(f"rule_{num}.json", "r") as rule_src:
        with open(f"rule_{num}_quoted.json", "w") as rule_quoted:
            for i, line in enumerate(rule_src):
                if line[0] != "}":
                    rule_quoted.write(line.replace("\n", "").lstrip() + "\n")
                else:
                    rule_quoted.write(line.replace("\n", "").lstrip() + "\n")


generate(
    event_num=200,
    field_len_max=1000,
    value_len_max=100,
    kwargs={
        "exact": 0,
        "prefix": 0,
        "suffix": 0,
        "equals-ignore-case": 0,
        "wildcard": 32,
        "anything-but": 0,
        "numeric": 0,
    },
)

for i in range(1, 1000, 5):
    add_quotes_to_rule(i)
