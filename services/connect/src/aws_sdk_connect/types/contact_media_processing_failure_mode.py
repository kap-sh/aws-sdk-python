"""Generated from Smithy shape ``com.amazonaws.connect#ContactMediaProcessingFailureMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_connect.errors import DeserializationError

ContactMediaProcessingFailureMode: TypeAlias = Literal[
    "DELIVER_UNPROCESSED_MESSAGE",
    "DO_NOT_DELIVER_UNPROCESSED_MESSAGE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DELIVER_UNPROCESSED_MESSAGE",
        "DO_NOT_DELIVER_UNPROCESSED_MESSAGE",
    )
)


def serialize_json(value: ContactMediaProcessingFailureMode) -> str:
    return value


def deserialize_json(data: str) -> ContactMediaProcessingFailureMode:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown ContactMediaProcessingFailureMode value: {data!r}"
        )
    return cast(ContactMediaProcessingFailureMode, data)
