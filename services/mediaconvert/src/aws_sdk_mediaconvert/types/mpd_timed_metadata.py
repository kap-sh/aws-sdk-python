"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdTimedMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank."""
MpdTimedMetadata: TypeAlias = Literal[
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


def serialize_json(value: MpdTimedMetadata) -> str:
    return value


def deserialize_json(data: str) -> MpdTimedMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MpdTimedMetadata value: {data!r}")
    return cast(MpdTimedMetadata, data)
