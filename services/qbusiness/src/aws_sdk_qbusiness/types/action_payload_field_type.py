"""Generated from Smithy shape ``com.amazonaws.qbusiness#ActionPayloadFieldType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ActionPayloadFieldType: TypeAlias = Literal[
    "STRING",
    "NUMBER",
    "ARRAY",
    "BOOLEAN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STRING",
        "NUMBER",
        "ARRAY",
        "BOOLEAN",
    )
)


def serialize_json(value: ActionPayloadFieldType) -> str:
    return value


def deserialize_json(data: str) -> ActionPayloadFieldType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ActionPayloadFieldType value: {data!r}")
    return cast(ActionPayloadFieldType, data)
