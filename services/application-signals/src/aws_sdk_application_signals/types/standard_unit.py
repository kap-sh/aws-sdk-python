"""Generated from Smithy shape ``com.amazonaws.applicationsignals#StandardUnit``."""

from typing import Literal, TypeAlias, cast

StandardUnit: TypeAlias = Literal[
    "Microseconds",
    "Milliseconds",
    "Seconds",
    "Bytes",
    "Kilobytes",
    "Megabytes",
    "Gigabytes",
    "Terabytes",
    "Bits",
    "Kilobits",
    "Megabits",
    "Gigabits",
    "Terabits",
    "Percent",
    "Count",
    "Bytes/Second",
    "Kilobytes/Second",
    "Megabytes/Second",
    "Gigabytes/Second",
    "Terabytes/Second",
    "Bits/Second",
    "Kilobits/Second",
    "Megabits/Second",
    "Gigabits/Second",
    "Terabits/Second",
    "Count/Second",
    "None",
]


# --- restJson1 ser/de ---
def serialize_json(value: StandardUnit) -> str:
    return value


def deserialize_json(data: str) -> StandardUnit:
    return cast(StandardUnit, data)
