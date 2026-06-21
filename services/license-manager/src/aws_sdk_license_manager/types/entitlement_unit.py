"""Generated from Smithy shape ``com.amazonaws.licensemanager#EntitlementUnit``."""

from typing import Literal, TypeAlias, cast

EntitlementUnit: TypeAlias = Literal[
    "Count",
    "None",
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
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntitlementUnit) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntitlementUnit:
    return cast(EntitlementUnit, data)
