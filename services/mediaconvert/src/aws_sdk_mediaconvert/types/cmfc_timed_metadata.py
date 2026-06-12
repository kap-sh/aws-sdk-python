"""Generated from Smithy shape ``com.amazonaws.mediaconvert#CmfcTimedMetadata``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediaconvert.errors import DeserializationError

"""To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank."""
CmfcTimedMetadata: TypeAlias = Literal[
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


def serialize_json(value: CmfcTimedMetadata) -> str:
    return value


def deserialize_json(data: str) -> CmfcTimedMetadata:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CmfcTimedMetadata value: {data!r}")
    return cast(CmfcTimedMetadata, data)
