"""Generated from Smithy shape ``com.amazonaws.iot#FleetMetricUnit``."""

from typing import Literal, TypeAlias, cast

FleetMetricUnit: TypeAlias = Literal[
    "Seconds",
    "Microseconds",
    "Milliseconds",
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
def serialize_json(value: FleetMetricUnit) -> str:
    return value


def deserialize_json(data: str) -> FleetMetricUnit:
    return cast(FleetMetricUnit, data)
