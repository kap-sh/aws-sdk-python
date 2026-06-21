"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHDisplayFragmentNumber``."""

from typing import Literal, TypeAlias, cast

DASHDisplayFragmentNumber: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- restJson1 ser/de ---
def serialize_json(value: DASHDisplayFragmentNumber) -> str:
    return value


def deserialize_json(data: str) -> DASHDisplayFragmentNumber:
    return cast(DASHDisplayFragmentNumber, data)
