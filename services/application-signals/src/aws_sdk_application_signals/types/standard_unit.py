"""Generated from Smithy shape ``com.amazonaws.applicationsignals#StandardUnit``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_application_signals.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_json(value: StandardUnit) -> str:
    return value


def deserialize_json(data: str) -> StandardUnit:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StandardUnit value: {data!r}")
    return cast(StandardUnit, data)
