"""Generated from Smithy shape ``com.amazonaws.clouddirectory#ObjectType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_clouddirectory.errors import DeserializationError

ObjectType: TypeAlias = Literal[
    "NODE",
    "LEAF_NODE",
    "POLICY",
    "INDEX",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NODE",
        "LEAF_NODE",
        "POLICY",
        "INDEX",
    )
)


def serialize_json(value: ObjectType) -> str:
    return value


def deserialize_json(data: str) -> ObjectType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ObjectType value: {data!r}")
    return cast(ObjectType, data)
