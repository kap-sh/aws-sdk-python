"""Generated from Smithy shape ``com.amazonaws.lightsail#MetricUnit``."""

from typing import Literal, TypeAlias, cast

MetricUnit: TypeAlias = Literal[
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MetricUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MetricUnit:
    return cast(MetricUnit, data)
