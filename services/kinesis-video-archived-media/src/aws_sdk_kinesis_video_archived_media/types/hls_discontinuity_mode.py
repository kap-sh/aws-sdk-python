"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSDiscontinuityMode``."""

from typing import Literal, TypeAlias, cast

HLSDiscontinuityMode: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
    "ON_DISCONTINUITY",
]


# --- restJson1 ser/de ---
def serialize_json(value: HLSDiscontinuityMode) -> str:
    return value


def deserialize_json(data: str) -> HLSDiscontinuityMode:
    return cast(HLSDiscontinuityMode, data)
