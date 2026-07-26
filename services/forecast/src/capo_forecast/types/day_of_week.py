"""Generated from Smithy shape ``com.amazonaws.forecast#DayOfWeek``."""

from typing import Literal, TypeAlias, cast

DayOfWeek: TypeAlias = Literal[
    "MONDAY",
    "TUESDAY",
    "WEDNESDAY",
    "THURSDAY",
    "FRIDAY",
    "SATURDAY",
    "SUNDAY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DayOfWeek) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DayOfWeek:
    return cast(DayOfWeek, data)
