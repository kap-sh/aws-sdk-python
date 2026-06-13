"""Generated from Smithy shape ``com.amazonaws.qbusiness#ChatResponseConfigurationStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_qbusiness.errors import DeserializationError

ChatResponseConfigurationStatus: TypeAlias = Literal[
    "CREATING",
    "UPDATING",
    "FAILED",
    "ACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "CREATING",
        "UPDATING",
        "FAILED",
        "ACTIVE",
    )
)


def serialize_json(value: ChatResponseConfigurationStatus) -> str:
    return value


def deserialize_json(data: str) -> ChatResponseConfigurationStatus:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ChatResponseConfigurationStatus value: {data!r}"
        )
    return cast(ChatResponseConfigurationStatus, data)
