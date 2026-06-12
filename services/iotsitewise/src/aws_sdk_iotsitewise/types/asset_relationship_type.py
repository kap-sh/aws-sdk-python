"""Generated from Smithy shape ``com.amazonaws.iotsitewise#AssetRelationshipType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iotsitewise.errors import DeserializationError

AssetRelationshipType: TypeAlias = Literal["HIERARCHY",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("HIERARCHY",))


def serialize_json(value: AssetRelationshipType) -> str:
    return value


def deserialize_json(data: str) -> AssetRelationshipType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AssetRelationshipType value: {data!r}")
    return cast(AssetRelationshipType, data)
