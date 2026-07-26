"""Generated from Smithy shape ``com.amazonaws.odb#MonthName``."""

from typing import Literal, TypeAlias, cast

MonthName: TypeAlias = Literal[
    "JANUARY",
    "FEBRUARY",
    "MARCH",
    "APRIL",
    "MAY",
    "JUNE",
    "JULY",
    "AUGUST",
    "SEPTEMBER",
    "OCTOBER",
    "NOVEMBER",
    "DECEMBER",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MonthName) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> MonthName:
    return cast(MonthName, data)
