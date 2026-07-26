"""Generated from Smithy shape ``com.amazonaws.mediaconvert#MpdTimedMetadata``."""

from typing import Literal, TypeAlias, cast

"""To include ID3 metadata in this output: Set ID3 metadata to Passthrough. Specify this ID3 metadata in Custom ID3 metadata inserter. MediaConvert writes each instance of ID3 metadata in a separate Event Message (eMSG) box. To exclude this ID3 metadata: Set ID3 metadata to None or leave blank."""
MpdTimedMetadata: TypeAlias = Literal[
    "PASSTHROUGH",
    "NONE",
]


# --- restJson1 ser/de ---
def serialize_json(value: MpdTimedMetadata) -> str:
    return value


def deserialize_json(data: str) -> MpdTimedMetadata:
    return cast(MpdTimedMetadata, data)
