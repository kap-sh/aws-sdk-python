"""Generated from Smithy shape ``com.amazonaws.bedrock#InferenceProfileType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_bedrock.errors import DeserializationError

InferenceProfileType: TypeAlias = Literal[
    "SYSTEM_DEFINED",
    "APPLICATION",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYSTEM_DEFINED",
        "APPLICATION",
    )
)


def serialize_json(value: InferenceProfileType) -> str:
    return value


def deserialize_json(data: str) -> InferenceProfileType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown InferenceProfileType value: {data!r}")
    return cast(InferenceProfileType, data)
