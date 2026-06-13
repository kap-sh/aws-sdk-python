"""Generated from Smithy shape ``com.amazonaws.bedrock#GuardrailStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

GuardrailStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "VERSIONING",
    "READY",
    "FAILED",
    "DELETING",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "VERSIONING",
        "READY",
        "FAILED",
        "DELETING",
    )
)


def serialize_json(value: GuardrailStatus) -> str:
    return value


def deserialize_json(data: str) -> GuardrailStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown GuardrailStatus value: {data!r}")
    return cast(GuardrailStatus, data)
