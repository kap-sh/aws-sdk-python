"""Generated from Smithy shape ``com.amazonaws.forecast#Month``."""

from typing import Literal, TypeAlias, cast

Month: TypeAlias = Literal[
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


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Month) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Month:
    return cast(Month, data)
