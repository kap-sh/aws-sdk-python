"""Generated from Smithy shape ``com.amazonaws.kinesisvideomedia#StartSelectorType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kinesis_video_media.errors import DeserializationError

StartSelectorType: TypeAlias = Literal[
    "FRAGMENT_NUMBER",
    "SERVER_TIMESTAMP",
    "PRODUCER_TIMESTAMP",
    "NOW",
    "EARLIEST",
    "CONTINUATION_TOKEN",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "FRAGMENT_NUMBER",
        "SERVER_TIMESTAMP",
        "PRODUCER_TIMESTAMP",
        "NOW",
        "EARLIEST",
        "CONTINUATION_TOKEN",
    )
)


def serialize_json(value: StartSelectorType) -> str:
    return value


def deserialize_json(data: str) -> StartSelectorType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown StartSelectorType value: {data!r}")
    return cast(StartSelectorType, data)
