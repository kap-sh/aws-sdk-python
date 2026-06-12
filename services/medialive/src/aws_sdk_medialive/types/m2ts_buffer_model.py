"""Generated from Smithy shape ``com.amazonaws.medialive#M2tsBufferModel``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_medialive.errors import DeserializationError

"""M2ts Buffer Model"""
M2tsBufferModel: TypeAlias = Literal[
    "MULTIPLEX",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MULTIPLEX",
        "NONE",
    )
)


def serialize_json(value: M2tsBufferModel) -> str:
    return value


def deserialize_json(data: str) -> M2tsBufferModel:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsBufferModel value: {data!r}")
    return cast(M2tsBufferModel, data)
