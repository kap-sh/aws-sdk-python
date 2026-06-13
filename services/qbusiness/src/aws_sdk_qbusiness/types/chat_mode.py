"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ChatMode: TypeAlias = Literal[
    "RETRIEVAL_MODE",
    "CREATOR_MODE",
    "PLUGIN_MODE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RETRIEVAL_MODE",
        "CREATOR_MODE",
        "PLUGIN_MODE",
    )
)


def serialize_json(value: ChatMode) -> str:
    return value


def deserialize_json(data: str) -> ChatMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ChatMode value: {data!r}")
    return cast(ChatMode, data)
