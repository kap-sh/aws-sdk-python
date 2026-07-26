"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHDisplayFragmentTimestamp``."""

from typing import Literal, TypeAlias, cast

DASHDisplayFragmentTimestamp: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: DASHDisplayFragmentTimestamp) -> str:
    return value


def deserialize_json(data: str) -> DASHDisplayFragmentTimestamp:
    return cast(DASHDisplayFragmentTimestamp, data)
