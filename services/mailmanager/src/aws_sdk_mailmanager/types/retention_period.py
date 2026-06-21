"""Generated from Smithy shape ``com.amazonaws.mailmanager#RetentionPeriod``."""

from typing import Literal, TypeAlias, cast

RetentionPeriod: TypeAlias = Literal[
    "THREE_MONTHS",
    "SIX_MONTHS",
    "NINE_MONTHS",
    "ONE_YEAR",
    "EIGHTEEN_MONTHS",
    "TWO_YEARS",
    "THIRTY_MONTHS",
    "THREE_YEARS",
    "FOUR_YEARS",
    "FIVE_YEARS",
    "SIX_YEARS",
    "SEVEN_YEARS",
    "EIGHT_YEARS",
    "NINE_YEARS",
    "TEN_YEARS",
    "PERMANENT",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RetentionPeriod) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RetentionPeriod:
    return cast(RetentionPeriod, data)
