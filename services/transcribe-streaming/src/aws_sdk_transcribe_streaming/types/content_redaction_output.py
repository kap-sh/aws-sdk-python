"""Generated from Smithy shape ``com.amazonaws.transcribestreaming#ContentRedactionOutput``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transcribe_streaming.errors import DeserializationError

ContentRedactionOutput: TypeAlias = Literal[
    "redacted",
    "redacted_and_unredacted",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "redacted",
        "redacted_and_unredacted",
    )
)


def serialize_json(value: ContentRedactionOutput) -> str:
    return value


def deserialize_json(data: str) -> ContentRedactionOutput:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ContentRedactionOutput value: {data!r}")
    return cast(ContentRedactionOutput, data)
