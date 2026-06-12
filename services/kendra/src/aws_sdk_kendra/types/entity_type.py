"""Generated from Smithy shape ``com.amazonaws.kendra#EntityType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kendra.errors import DeserializationError

EntityType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "USER",
        "GROUP",
    )
)


def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EntityType value: {data!r}")
    return cast(EntityType, data)
