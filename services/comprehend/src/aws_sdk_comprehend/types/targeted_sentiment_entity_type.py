"""Generated from Smithy shape ``com.amazonaws.comprehend#TargetedSentimentEntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

TargetedSentimentEntityType: TypeAlias = Literal[
    "PERSON",
    "LOCATION",
    "ORGANIZATION",
    "FACILITY",
    "BRAND",
    "COMMERCIAL_ITEM",
    "MOVIE",
    "MUSIC",
    "BOOK",
    "SOFTWARE",
    "GAME",
    "PERSONAL_TITLE",
    "EVENT",
    "DATE",
    "QUANTITY",
    "ATTRIBUTE",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "FACILITY",
        "BRAND",
        "COMMERCIAL_ITEM",
        "MOVIE",
        "MUSIC",
        "BOOK",
        "SOFTWARE",
        "GAME",
        "PERSONAL_TITLE",
        "EVENT",
        "DATE",
        "QUANTITY",
        "ATTRIBUTE",
        "OTHER",
    )
)


def serialize_aws_json_1_1(value: TargetedSentimentEntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> TargetedSentimentEntityType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown TargetedSentimentEntityType value: {data!r}"
        )
    return cast(TargetedSentimentEntityType, data)
