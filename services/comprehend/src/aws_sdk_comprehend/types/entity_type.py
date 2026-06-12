"""Generated from Smithy shape ``com.amazonaws.comprehend#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_comprehend.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "PERSON",
    "LOCATION",
    "ORGANIZATION",
    "COMMERCIAL_ITEM",
    "EVENT",
    "DATE",
    "QUANTITY",
    "TITLE",
    "OTHER",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PERSON",
        "LOCATION",
        "ORGANIZATION",
        "COMMERCIAL_ITEM",
        "EVENT",
        "DATE",
        "QUANTITY",
        "TITLE",
        "OTHER",
    )
)


def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
