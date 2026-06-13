"""Generated from Smithy shape ``com.amazonaws.mailmanager#RetentionPeriod``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mailmanager.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_0(value: RetentionPeriod) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> RetentionPeriod:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RetentionPeriod value: {data!r}")
    return cast(RetentionPeriod, data)
