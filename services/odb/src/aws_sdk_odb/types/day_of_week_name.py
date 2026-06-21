"""Generated from Smithy shape ``com.amazonaws.odb#DayOfWeekName``."""

from typing import Literal, TypeAlias, cast

DayOfWeekName: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DayOfWeekName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> DayOfWeekName:
    return cast(DayOfWeekName, data)
