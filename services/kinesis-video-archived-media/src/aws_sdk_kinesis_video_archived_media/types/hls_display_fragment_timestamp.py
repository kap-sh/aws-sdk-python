"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSDisplayFragmentTimestamp``."""

from typing import Literal, TypeAlias, cast

HLSDisplayFragmentTimestamp: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: HLSDisplayFragmentTimestamp) -> str:
    return value


def deserialize_json(data: str) -> HLSDisplayFragmentTimestamp:
    return cast(HLSDisplayFragmentTimestamp, data)
