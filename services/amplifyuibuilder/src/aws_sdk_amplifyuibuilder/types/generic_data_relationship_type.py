"""Generated from Smithy shape ``com.amazonaws.amplifyuibuilder#GenericDataRelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplifyuibuilder.errors import DeserializationError

GenericDataRelationshipType: TypeAlias = Literal[
    "HAS_MANY",
    "HAS_ONE",
    "BELONGS_TO",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HAS_MANY",
        "HAS_ONE",
        "BELONGS_TO",
    )
)


def serialize_json(value: GenericDataRelationshipType) -> str:
    return value


def deserialize_json(data: str) -> GenericDataRelationshipType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown GenericDataRelationshipType value: {data!r}"
        )
    return cast(GenericDataRelationshipType, data)
