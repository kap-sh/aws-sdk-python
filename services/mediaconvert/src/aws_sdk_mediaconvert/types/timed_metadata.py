"""Generated from Smithy shape ``com.amazonaws.mediaconvert#TimedMetadata``."""

from typing import Literal, TypeAlias, cast

"""Set ID3 metadata to Passthrough to include ID3 metadata in this output. This includes ID3 metadata from the following features: ID3 timestamp period, and Custom ID3 metadata inserter. To exclude this ID3 metadata in this output: set ID3 metadata to None or leave blank."""
TimedMetadata: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: TimedMetadata) -> str:
    return value


def deserialize_json(data: str) -> TimedMetadata:
    return cast(TimedMetadata, data)
