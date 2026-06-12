"""Generated from Smithy shape ``com.amazonaws.customerprofiles#RecommenderSchemaStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_customer_profiles.errors import DeserializationError

RecommenderSchemaStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "DELETING",
    )
)


def serialize_json(value: RecommenderSchemaStatus) -> str:
    return value


def deserialize_json(data: str) -> RecommenderSchemaStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown RecommenderSchemaStatus value: {data!r}")
    return cast(RecommenderSchemaStatus, data)
