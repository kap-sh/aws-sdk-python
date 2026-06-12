"""Generated from Smithy shape ``com.amazonaws.mediaconvert#M2tsKlvMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To include key-length-value metadata in this output: Set KLV metadata insertion to Passthrough. MediaConvert reads KLV metadata present in your input and passes it through to the output transport stream. To exclude this KLV metadata: Set KLV metadata insertion to None or leave blank."""
M2tsKlvMetadata: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PASSTHROUGH",
        "NONE",
    )
)


def serialize_json(value: M2tsKlvMetadata) -> str:
    return value


def deserialize_json(data: str) -> M2tsKlvMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown M2tsKlvMetadata value: {data!r}")
    return cast(M2tsKlvMetadata, data)
