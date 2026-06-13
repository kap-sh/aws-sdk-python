"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

InferenceType: TypeAlias = Literal[
    "ON_DEMAND",
    "PROVISIONED",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ON_DEMAND",
        "PROVISIONED",
    )
)


def serialize_json(value: InferenceType) -> str:
    return value


def deserialize_json(data: str) -> InferenceType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceType value: {data!r}")
    return cast(InferenceType, data)
