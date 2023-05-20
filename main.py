import json
import logging
import random
import string
from enum import Enum

import numpy as np

# l = np.array([1738, 1740, 1733, 1725, 1745, 1721, 1744, 1717, 1722, 1741])

# l = np.array([29879.1, 29441.5, 27567.3, 26950.2, 29883.3, 30124.1, 29642.2, 29502.6, 29079.8, 26868.6])
# l = np.array([244745.0, 242004.9, 244785.2, 241534.6, 243387.1, 245147.3, 243984.3, 242004.9, 242319.4, 242240.7])

EXACT = []
WILDCARD = []
PREFIX = []
SUFFIX = []
EQUALS_IGNORE_CASE = []
NUMERIC = []
ANYTHING_BUT = []
ANYTHING_BUT_PREFIX = []
ANYTHING_BUT_SUFFIX = []
COMPLEX_ARRAYS = []
PARTIAL_COMBO = []
COMBO = []

patterns = [EXACT, WILDCARD, PREFIX, SUFFIX, EQUALS_IGNORE_CASE, NUMERIC, ANYTHING_BUT, ANYTHING_BUT_PREFIX,
            ANYTHING_BUT_SUFFIX,
            COMPLEX_ARRAYS, PARTIAL_COMBO, COMBO]


def parse(s: str):
    l = s.split('\n')
    l = l[2:]
    for i in range(len(l)):
        x = l[i]
        y = l[i].split(' ')[2]
        num = l[i].split(' ')[2].replace(',', '.')
        # print(num)
        patterns[i].append(float(num))


s1 = """Reading citylots2
Read 213068 events
EXACT events/sec: 421083,0
WILDCARD events/sec: 294292,8
PREFIX events/sec: 448564,2
SUFFIX events/sec: 455273,5
EQUALS_IGNORE_CASE events/sec: 388102,0
NUMERIC events/sec: 264352,4
ANYTHING-BUT events/sec: 255477,2
ANYTHING-BUT-PREFIX events/sec: 268347,6
ANYTHING-BUT-SUFFIX events/sec: 259206,8
COMPLEX_ARRAYS events/sec: 7901,9
PARTIAL_COMBO events/sec: 173791,2
COMBO events/sec: 4809,2"""
s2 = """"Reading citylots2
Read 213068 events
EXACT events/sec: 465214,0
WILDCARD events/sec: 311959,0
PREFIX events/sec: 452373,7
SUFFIX events/sec: 460190,1
EQUALS_IGNORE_CASE events/sec: 389521,0
NUMERIC events/sec: 268686,0
ANYTHING-BUT events/sec: 256708,4
ANYTHING-BUT-PREFIX events/sec: 270390,9
ANYTHING-BUT-SUFFIX events/sec: 259839,0
COMPLEX_ARRAYS events/sec: 7535,0
PARTIAL_COMBO events/sec: 171139,0
COMBO events/sec: 5063,8"""
s3 = """Reading citylots2
Read 213068 events
EXACT events/sec: 455273,5
WILDCARD events/sec: 306132,2
PREFIX events/sec: 446683,4
SUFFIX events/sec: 457227,5
EQUALS_IGNORE_CASE events/sec: 373803,5
NUMERIC events/sec: 259522,5
ANYTHING-BUT events/sec: 259206,8
ANYTHING-BUT-PREFIX events/sec: 272117,5
ANYTHING-BUT-SUFFIX events/sec: 258891,9
COMPLEX_ARRAYS events/sec: 8229,4
PARTIAL_COMBO events/sec: 181180,3
COMBO events/sec: 4851,7"""
s4 = """Reading citylots2
Read 213068 events
EXACT events/sec: 460190,1
WILDCARD events/sec: 306132,2
PREFIX events/sec: 442049,8
SUFFIX events/sec: 438411,5
EQUALS_IGNORE_CASE events/sec: 349865,4
NUMERIC events/sec: 270048,2
ANYTHING-BUT events/sec: 255171,3
ANYTHING-BUT-PREFIX events/sec: 233883,6
ANYTHING-BUT-SUFFIX events/sec: 253954,7
COMPLEX_ARRAYS events/sec: 8061,9
PARTIAL_COMBO events/sec: 181334,5
COMBO events/sec: 4901,3"""
s5 = """Reading citylots2
Read 213068 events
EXACT events/sec: 453336,2
WILDCARD events/sec: 309691,9
PREFIX events/sec: 430440,4
SUFFIX events/sec: 455273,5
EQUALS_IGNORE_CASE events/sec: 365468,3
NUMERIC events/sec: 258264,2
ANYTHING-BUT events/sec: 249202,3
ANYTHING-BUT-PREFIX events/sec: 261112,7
ANYTHING-BUT-SUFFIX events/sec: 251259,4
COMPLEX_ARRAYS events/sec: 7938,2
PARTIAL_COMBO events/sec: 173933,1
COMBO events/sec: 4932,9"""
s6 = """Reading citylots2
Read 213068 events
EXACT events/sec: 423594,4
WILDCARD events/sec: 303083,9
PREFIX events/sec: 435721,9
SUFFIX events/sec: 444818,4
EQUALS_IGNORE_CASE events/sec: 377780,1
NUMERIC events/sec: 259839,0
ANYTHING-BUT events/sec: 253049,9
ANYTHING-BUT-PREFIX events/sec: 261754,3
ANYTHING-BUT-SUFFIX events/sec: 253350,8
COMPLEX_ARRAYS events/sec: 7934,0
PARTIAL_COMBO events/sec: 173508,1
COMBO events/sec: 4576,3"""
s7 = """Reading citylots2
Read 213068 events
EXACT events/sec: 459198,3
WILDCARD events/sec: 306132,2
PREFIX events/sec: 416962,8
SUFFIX events/sec: 305255,0
EQUALS_IGNORE_CASE events/sec: 201387,5
NUMERIC events/sec: 268010,1
ANYTHING-BUT events/sec: 255477,2
ANYTHING-BUT-PREFIX events/sec: 266335,0
ANYTHING-BUT-SUFFIX events/sec: 257018,1
COMPLEX_ARRAYS events/sec: 7687,5
PARTIAL_COMBO events/sec: 176089,3
COMBO events/sec: 4887,6"""
s8 = """Reading citylots2
Read 213068 events
EXACT events/sec: 356897,8
WILDCARD events/sec: 162028,9
PREFIX events/sec: 400503,8
SUFFIX events/sec: 420252,5
EQUALS_IGNORE_CASE events/sec: 361745,3
NUMERIC events/sec: 267673,4
ANYTHING-BUT events/sec: 250079,8
ANYTHING-BUT-PREFIX events/sec: 258891,9
ANYTHING-BUT-SUFFIX events/sec: 236479,5
COMPLEX_ARRAYS events/sec: 7960,7
PARTIAL_COMBO events/sec: 180872,7
COMBO events/sec: 4853,4"""

s9 = """"Reading citylots2
Read 213068 events
EXACT events/sec: 462186,6
WILDCARD events/sec: 308794,2
PREFIX events/sec: 446683,4
SUFFIX events/sec: 459198,3
EQUALS_IGNORE_CASE events/sec: 388810,2
NUMERIC events/sec: 261754,3
ANYTHING-BUT events/sec: 251556,1
ANYTHING-BUT-PREFIX events/sec: 267337,5
ANYTHING-BUT-SUFFIX events/sec: 259206,8
COMPLEX_ARRAYS events/sec: 8191,1
PARTIAL_COMBO events/sec: 176526,9
COMBO events/sec: 4756,5"""
s10 = """Reading citylots2
Read 213068 events
EXACT events/sec: 446683,4
WILDCARD events/sec: 307014,4
PREFIX events/sec: 433947,0
SUFFIX events/sec: 451415,3
EQUALS_IGNORE_CASE events/sec: 384599,3
NUMERIC events/sec: 267673,4
ANYTHING-BUT events/sec: 254257,8
ANYTHING-BUT-PREFIX events/sec: 269025,3
ANYTHING-BUT-SUFFIX events/sec: 258264,2
COMPLEX_ARRAYS events/sec: 8218,3
PARTIAL_COMBO events/sec: 181643,6
COMBO events/sec: 5046,3"""
# sn = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
# for s in sn:
#     parse(s)
#
# for p in patterns:
#     p = np.array(p)
#     print(round(p.mean(), 1))
#     print(round(p.std(), 1))
#     print('\n')

# l = np.array([1667, 1668, 1668, 1669, 1667, 1667, 1668, 1668, 1668, 1667])
# print(l.mean())
# print(l.std())
# print(3047/1668)
# l = np.array([12500, 11111, 14285, 12500, 10000, 8333, 5882, 9090, 11111, 11111])
# print(l.mean())
# print(l.std())

new1 = """Reading citylots2
Read 213068 events
EXACT events/sec: 97917,3
WILDCARD events/sec: 91367,1
PREFIX events/sec: 98688,3
SUFFIX events/sec: 98414,8
EQUALS_IGNORE_CASE events/sec: 96193,2
NUMERIC events/sec: 86683,5
ANYTHING-BUT events/sec: 78768,2
ANYTHING-BUT-PREFIX events/sec: 61033,5
ANYTHING-BUT-SUFFIX events/sec: 86683,5
COMPLEX_ARRAYS events/sec: 4853,5
PARTIAL_COMBO events/sec: 71812,6
COMBO events/sec: 4927,6"""
new2 = """Reading citylots2
Read 213068 events
EXACT events/sec: 100836,7
WILDCARD events/sec: 92718,9
PREFIX events/sec: 101751,7
SUFFIX events/sec: 100741,4
EQUALS_IGNORE_CASE events/sec: 94570,8
NUMERIC events/sec: 89112,5
ANYTHING-BUT events/sec: 87538,2
ANYTHING-BUT-PREFIX events/sec: 89637,4
ANYTHING-BUT-SUFFIX events/sec: 88117,5
COMPLEX_ARRAYS events/sec: 5015,6
PARTIAL_COMBO events/sec: 79001,9
COMBO events/sec: 4954,4"""
new3 = """Reading citylots2
Read 213068 events
EXACT events/sec: 98188,0
WILDCARD events/sec: 91132,6
PREFIX events/sec: 98825,6
SUFFIX events/sec: 98188,0
EQUALS_IGNORE_CASE events/sec: 95717,9
NUMERIC events/sec: 87610,2
ANYTHING-BUT events/sec: 87754,5
ANYTHING-BUT-PREFIX events/sec: 88963,7
ANYTHING-BUT-SUFFIX events/sec: 87899,3
COMPLEX_ARRAYS events/sec: 4607,0
PARTIAL_COMBO events/sec: 76478,1
COMBO events/sec: 4691,8"""
new4 = """Reading citylots2
Read 213068 events
EXACT events/sec: 72104,2
WILDCARD events/sec: 67662,1
PREFIX events/sec: 95077,2
SUFFIX events/sec: 93862,6
EQUALS_IGNORE_CASE events/sec: 96981,3
NUMERIC events/sec: 88117,5
ANYTHING-BUT events/sec: 87718,4
ANYTHING-BUT-PREFIX events/sec: 89486,8
ANYTHING-BUT-SUFFIX events/sec: 88190,4
COMPLEX_ARRAYS events/sec: 5013,5
PARTIAL_COMBO events/sec: 72398,2
COMBO events/sec: 4670,5"""
new5 = """Reading citylots2
Read 213068 events
EXACT events/sec: 87574,2
WILDCARD events/sec: 92317,2
PREFIX events/sec: 98688,3
SUFFIX events/sec: 97648,0
EQUALS_IGNORE_CASE events/sec: 97291,3
NUMERIC events/sec: 88667,5
ANYTHING-BUT events/sec: 88556,9
ANYTHING-BUT-PREFIX events/sec: 89788,5
ANYTHING-BUT-SUFFIX events/sec: 88630,6
COMPLEX_ARRAYS events/sec: 4835,6
PARTIAL_COMBO events/sec: 73093,7
COMBO events/sec: 4727,9"""
new6 = """Reading citylots2
Read 213068 events
EXACT events/sec: 98278,6
WILDCARD events/sec: 87971,9
PREFIX events/sec: 97648,0
SUFFIX events/sec: 94277,9
EQUALS_IGNORE_CASE events/sec: 84017,4
NUMERIC events/sec: 68976,4
ANYTHING-BUT events/sec: 84685,2
ANYTHING-BUT-PREFIX events/sec: 87180,0
ANYTHING-BUT-SUFFIX events/sec: 83457,9
COMPLEX_ARRAYS events/sec: 4985,4
PARTIAL_COMBO events/sec: 76670,7
COMBO events/sec: 4896,2"""
new7 = """Reading citylots2
Read 213068 events
EXACT events/sec: 76259,1
WILDCARD events/sec: 58422,8
PREFIX events/sec: 96193,2
SUFFIX events/sec: 96629,5
EQUALS_IGNORE_CASE events/sec: 93986,8
NUMERIC events/sec: 86931,0
ANYTHING-BUT events/sec: 87538,2
ANYTHING-BUT-PREFIX events/sec: 87826,9
ANYTHING-BUT-SUFFIX events/sec: 86367,2
COMPLEX_ARRAYS events/sec: 5012,1
PARTIAL_COMBO events/sec: 77932,7
COMBO events/sec: 4630,7"""
new8 = """Reading citylots2
Read 213068 events
EXACT events/sec: 95417,8
WILDCARD events/sec: 86472,4
PREFIX events/sec: 98779,8
SUFFIX events/sec: 98233,3
EQUALS_IGNORE_CASE events/sec: 96063,1
NUMERIC events/sec: 87037,6
ANYTHING-BUT events/sec: 86966,5
ANYTHING-BUT-PREFIX events/sec: 87502,3
ANYTHING-BUT-SUFFIX events/sec: 86718,8
COMPLEX_ARRAYS events/sec: 4794,1
PARTIAL_COMBO events/sec: 74007,6
COMBO events/sec: 4540,5"""

new9 = """Reading citylots2
Read 213068 events
EXACT events/sec: 100884,5
WILDCARD events/sec: 92197,3
PREFIX events/sec: 99378,7
SUFFIX events/sec: 98825,6
EQUALS_IGNORE_CASE events/sec: 96673,3
NUMERIC events/sec: 87682,3
ANYTHING-BUT events/sec: 80524,6
ANYTHING-BUT-PREFIX events/sec: 87323,0
ANYTHING-BUT-SUFFIX events/sec: 89038,0
COMPLEX_ARRAYS events/sec: 4773,7
PARTIAL_COMBO events/sec: 77394,8
COMBO events/sec: 4836,6"""

new10 = """Reading citylots2
Read 213068 events
EXACT events/sec: 98188,0
WILDCARD events/sec: 91879,3
PREFIX events/sec: 98324,0
SUFFIX events/sec: 97158,2
EQUALS_IGNORE_CASE events/sec: 96106,5
NUMERIC events/sec: 87251,4
ANYTHING-BUT events/sec: 87108,7
ANYTHING-BUT-PREFIX events/sec: 88446,7
ANYTHING-BUT-SUFFIX events/sec: 84550,8
COMPLEX_ARRAYS events/sec: 4927,5
PARTIAL_COMBO events/sec: 77961,2
COMBO events/sec: 4824,3"""

# newn = [new1, new2, new3, new4, new5, new6, new7, new8, new9, new10]
# for s in newn:
#     parse(s)
#
# for p in patterns:
#     p = np.array(p)
#     print(round(p.mean(), 1))
#     print(round(p.std(), 1))
#     print('\n')

before = """EXACT events/sec: 440365.7
WILDCARD events/sec: 291526.2
PREFIX events/sec: 435393.0
SUFFIX events/sec: 434731.6
EQUALS_IGNORE_CASE events/sec: 358108.3
NUMERIC events/sec: 264582.4
ANYTHING-BUT events/sec: 254018.7
ANYTHING-BUT-PREFIX events/sec: 262919.6
ANYTHING-BUT-SUFFIX events/sec: 254747.1
COMPLEX_ARRAYS events/sec: 7965.8
PARTIAL_COMBO events/sec: 177001.9
COMBO events/sec: 4867.9"""

after = """EXACT events/sec: 92564.8
WILDCARD events/sec: 85214.2
PREFIX events/sec: 98335.5
SUFFIX events/sec: 97397.9
EQUALS_IGNORE_CASE events/sec: 94760.2
NUMERIC events/sec: 85807.0
ANYTHING-BUT events/sec: 85715.9
ANYTHING-BUT-PREFIX events/sec: 85718.9
ANYTHING-BUT-SUFFIX events/sec: 86965.4
COMPLEX_ARRAYS events/sec: 4881.8
PARTIAL_COMBO events/sec: 75675.2
COMBO events/sec: 4770.0"""


# def compare():
#     bef = before.split('\n')
#     aft = after.split('\n')
#
#     for i in range(len(bef)):
#         num_bef = float(bef[i].split(' ')[2])
#         num_aft = float(aft[i].split(' ')[2])
#         print(bef[i].split(' ')[0] + " " + str(round((num_bef - num_aft) / num_bef * 100, 1)) + "%")
#
# compare()

def compare(d1, d2):
    if isinstance(d1, dict) and isinstance(d2, dict):
        if d1.keys() != d2.keys():
            return False
        for key in d1:
            if not compare(d1[key], d2[key]):
                return False
        return True
    elif not isinstance(d1, dict) and not isinstance(d2, dict):
        return True
    else:
        return False


# with open("/Users/karina/Desktop/citylots2.json", "r") as f:
#     data = []
#     for line in f:
#         data.append(json.loads(line))
#     for i in range(1, len(data)):
#         if not compare(data[0], data[i]):
#             print(f"NO: {i}\n" + data[i])
#     print("YES")
# s = ''.join(random.choice(string.ascii_lowercase) for _ in range(1000))

# with open("/Users/karina/Desktop/citylots2.json", "r") as f:
#     with open("test.json", "w") as new_file:
#         for line in f:
#             new_file.write(line.replace("properties",  s))
#
# with open("src.json", "w") as new_file:
#     new_file.write(s)

logging.basicConfig(filename='/Users/karina/seminars/pythonProject2/replace.log', filemode='a', level=logging.INFO)


def generate_to_replace(src: str, field_len):
    logging.info(f"Replacing by len {field_len}...")
    replace_all = dict()

    keys = ["x", "y", "z", "type", "properties", "MAPBLKLOT", "BLKLOT", "BLOCK_NUM", "LOT_NUM", "FROM_ST", "TO_ST",
            "STREET", "ST_TYPE", "ODD_EVEN", "geometry", "coordinates"]
    for key in keys:
        replace_all[key] = ''.join(random.choice(string.ascii_lowercase) for _ in range(field_len))
        src = src.replace(key, replace_all[key])
        logging.info(f"Field {key} replaced by:\n{replace_all[key]}")
    return src, replace_all


def generate_to_replace(field_len):
    logging.info(f"Replacing by len {field_len}...")
    replace_all = dict()

    keys = ["x", "y", "z", "type", "properties", "MAPBLKLOT", "BLKLOT", "BLOCK_NUM", "LOT_NUM", "FROM_ST", "TO_ST",
            "STREET", "ST_TYPE", "ODD_EVEN", "geometry", "coordinates", "firstCoordinates"]
    for key in keys:
        replace_all[key] = ''.join(random.choice(string.ascii_lowercase) for _ in range(field_len))
        logging.info(f"Field {key} replaced by:\n{replace_all[key]}")
    return replace_all


import re

# def find_nth_overlapping(haystack, needle, n):
#     start = haystack.find(needle)
#     while start >= 0 and n > 1:
#         start = haystack.find(needle, start + 1)
#         n -= 1
#     return start


# with open("/Users/karina/Desktop/citylots2.json", "r") as f:
#     with open("/Users/karina/Desktop/after_field_resize.json", "w") as after_file:
#         replaced_fields = generate_to_replace(10)
#         for line in f:
#             new_line = line
#             for field in re.split("{|,", line):
#                 # print(field)
#                 if not field or field.find("\"") == -1:
#                     continue
#                 first = find_nth_overlapping(field, "\"", 1)
#                 second = find_nth_overlapping(field, "\"", 2)
#                 new = f'{field[:first + 1]}{replaced_fields[field[first + 1: second]]}{field[second:]}'
#                 new_line = new_line.replace(field, new)
#             after_file.write(new_line)

s = """{"type":"Feature","properties":{"MAPBLKLOT":"0001001","BLKLOT":"0001001","BLOCK_NUM":"0001","LOT_NUM":"001",
"FROM_ST":"0","TO_ST":"0","STREET":"UNKNOWN","ST_TYPE":null,"ODD_EVEN":"E"},"geometry":{"type":"Polygon",
"coordinates":[[{"x":-122.42200352825247,"y":37.80848009696725,"z":0.0},{"x":-122.42207601332528,
"y":37.808835019815085,"z":0.0},{"x":-122.42110217434863,"y":37.808803534992904,"z":0.0},{"x":-122.42106256906727,
"y":37.80860105681815,"z":0.0},{"x":-122.42200352825247,"y":37.80848009696725,"z":0.0}]],"firstCoordinates":{
"x":-122.42200352825247,"y":37.80848009696725,"z":0.0}}}"""


class Type(Enum):
    EXACT = 1


# def generate_nested(rule_complex, events, field_len, kwargs, nested_layer):
#     if nested_layer == 0:
#         generate_one_line(rule_complex, events, field_len, kwargs)
#     else:
#         outer_field_name = "".join(random.choice(string.ascii_lowercase) for _ in range(field_len))
#         rule_complex.write("    \"" + new_filed + "\": " + "[ \"" + new_value + "\" ],\n")
#         events.write(" " * nested_layer + "\n" + outer_field_name + "\"{\n")
#         generate_nested(rule_complex, events, field_len, kwargs, nested_layer - 1)
#         events.write(" " * nested_layer + "}\n" )

from random import choice


def generate_one_line(rule_complex, events, field_len, value_len, kwargs: dict):
    rule_complex.write("{\n")
    events.write("{")

    rule_num = 0
    for r in kwargs.values():
        rule_num += r
    # print(rule_num)

    out = []

    if "exact" in kwargs.keys():
        for i in range(kwargs["exact"]):
            new_filed = "".join(random.choice(string.ascii_lowercase) for _ in range(field_len))
            new_value = "".join(random.choice(string.ascii_lowercase) for _ in range(value_len))

            out.append(list([new_filed, new_value]))

            if i < rule_num - 1:
                rule_complex.write("    \"" + new_filed + "\": " + "[ \"" + new_value + "\" ],\n")
                events.write("\"" + new_filed + "\":" + "\"" + new_value + "\",")
            else:
                rule_complex.write("    \"" + new_filed + "\": " + "[ \"" + new_value + "\" ]\n")
                events.write("\"" + new_filed + "\":" + "\"" + new_value + "\"")

    if "prefix" in kwargs.keys():
        for i in range(kwargs["prefix"]):
            new_filed = "".join(random.choice(string.ascii_lowercase) for _ in range(field_len))

            prefix_len = random.randint(1, value_len)
            no_prefix_len = field_len - prefix_len

            prefix = "".join(random.choice(string.ascii_lowercase) for _ in range(prefix_len))
            all_field_with_prefix = prefix + "".join(
                random.choice(string.ascii_lowercase) for _ in range(no_prefix_len))

            out.append(list([new_filed, all_field_with_prefix, "prefix"]))

            if kwargs["exact"] + i < rule_num - 1:
                rule_complex.write("    \"" + new_filed + "\": " + "[ {\"prefix\": \"" + prefix + "\" } ],\n")
                events.write("\"" + new_filed + "\":" + "\"" + all_field_with_prefix + "\",")
            else:
                rule_complex.write("    \"" + new_filed + "\": " + "[ {\"prefix\": \"" + prefix + "\" } ]\n")
                events.write("\"" + new_filed + "\":" + "\"" + all_field_with_prefix + "\"")
    if "suffix" in kwargs.keys():
        for i in range(kwargs["suffix"]):
            new_filed = "".join(random.choice(string.ascii_lowercase) for _ in range(field_len))

            prefix_len = random.randint(1, value_len)
            no_prefix_len = field_len - prefix_len

            prefix = "".join(random.choice(string.ascii_lowercase) for _ in range(prefix_len))
            all_field_with_prefix = "".join(
                random.choice(string.ascii_lowercase) for _ in range(no_prefix_len)) + prefix

            out.append(list([new_filed, all_field_with_prefix, "suffix"]))

            if kwargs["exact"] + + kwargs["prefix"] + i < rule_num - 1:
                rule_complex.write("    \"" + new_filed + "\": " + "[ {\"suffix\": \"" + prefix + "\" } ],\n")
                events.write("\"" + new_filed + "\":" + "\"" + all_field_with_prefix + "\",")
            else:
                rule_complex.write("    \"" + new_filed + "\": " + "[ {\"suffix\": \"" + prefix + "\" } ]\n")
                events.write("\"" + new_filed + "\":" + "\"" + all_field_with_prefix + "\"")
    if "equals-ignore-case" in kwargs.keys():
        for i in range(kwargs["equals-ignore-case"]):
            new_filed = "".join(random.choice(string.ascii_lowercase) for _ in range(field_len))
            new_value = "".join(random.choice(string.ascii_lowercase) for _ in range(value_len))
            new_value_random_case = "".join(choice((str.upper, str.lower))(c) for c in new_value)

            out.append(list([new_filed, new_value_random_case, "equals-ignore-case"]))

            if kwargs["exact"] + + kwargs["prefix"] + kwargs["suffix"] + i < rule_num - 1:
                rule_complex.write(
                    "    \"" + new_filed + "\": " + "[ {\"equals-ignore-case\": \"" + new_value + "\" } ],\n")
                events.write("\"" + new_filed + "\":" + "\"" + new_value_random_case + "\",")
            else:
                rule_complex.write(
                    "    \"" + new_filed + "\": " + "[ {\"equals-ignore-case\": \"" + new_value + "\" } ]\n")
                events.write("\"" + new_filed + "\":" + "\"" + new_value_random_case + "\"")
    rule_complex.write("}")
    events.write("}\n")
    return out


NUMERIC_TYPES = []


# будет беда если тип - не строка
def build_event(field: str, value: str, type="exact"):
    if type not in NUMERIC_TYPES:
        return f"\"{field}\": \"{value}\""


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
    return "".join(random.choice(string.ascii_lowercase) for _ in range(len(str_len)))


def change_value(pair):
    if len(pair) == 2 or pair[2] == "prefix" or pair[2] == "suffix" or pair[2] == "equals-ignore-case":
        pair[1] = generate_random_str(pair[1])


# {abc}
# {EXACT: 1}
def generate(event_num, field_len_max: int, value_len_max, kwargs):
    # for i in range(event_num):
    for field_len in range(1, field_len_max + 1, 5):
        with open(f"rule_{field_len}.json", "w") as rule_complex:
            with open(f"events_{field_len}.json", "w") as events:
                out = generate_one_line(rule_complex=rule_complex, events=events, field_len=field_len, value_len=value_len_max, kwargs=kwargs)
                # print(out)
                for i in range(event_num):
                    value_needs_change = np.random.choice([0, 1], size=len(out), p=[.99, .01])

                    for i in range(len(out)):
                        if value_needs_change[i] == 1:
                            change_value(out[i])

                    new = generate_from_out(out)
                    events.write(new)

                # for i in range()
                # print(change_value_num)

                # if i < event_num - 1:
                #     rule_complex.write(",\n")


import re


def count_match(event_num):
    with open(f"events_{event_num}.json", "r") as event_file:
        with open(f"match_{event_num}.json", "w") as match_file:
            for one_event in event_file:
                d = json.loads(one_event)

                for field, value in d.items():
                    with open(f"rule_{event_num}.json", "r") as rule_file:
                        for l in rule_file:
                            # print(f"l: {l}, field: {field}\n")
                            m = re.findall(f'{field}', l)
                            if len(m) > 0:
                                pass
                                # print(m)
                                # print(i)

# tmp = "\"ab"
# m = re.findall(f'ab', tmp)
# print(m)


generate(10, 1000, 100, {"exact": 100, "prefix"})

# count_match(6)


def add_quotes_to_rule(num):
    with open(f"rule_{num}.json", "r") as rule_src:
        with open(f"rule_{num}_quoted.json", "w") as rule_quoted:
            for i, line in enumerate(rule_src):
                if line[0] != "}":
                    rule_quoted.write(line.replace("\n", "").lstrip() + "\n")
                else:
                    rule_quoted.write(line.replace("\n", "").lstrip() + "\n")
                # if line[0] != "}":
                #     rule_quoted.write("\"" + line.replace("\n", "").replace("\"", "\\\"") + "\\n\" + \n")
                # else:
                #     rule_quoted.write("\"" + line.replace("\n", "").replace("\"", "\\\"") + "\\n\"\n")


for i in range(1, 1000, 5):
    add_quotes_to_rule(i)

# replaced_fields = generate_to_replace(10)
# for field in re.split("{|,", s):
#     if not field:
#         continue
#     first = find_nth_overlapping(field, "\"", 1)
#     second = find_nth_overlapping(field, "\"", 2)
#     new = f'{field[:first+1]}{replaced_fields[field[first+1: second]]}{field[second:]}'
#     # print(field)
#     s = s.replace(field, new)
#
# print(s)
