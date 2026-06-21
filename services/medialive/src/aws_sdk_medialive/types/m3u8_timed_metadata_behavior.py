"""Generated from Smithy shape ``com.amazonaws.medialive#M3u8TimedMetadataBehavior``."""

from typing import Literal, TypeAlias, cast

"""M3u8 Timed Metadata Behavior"""
M3u8TimedMetadataBehavior: TypeAlias = Literal[
    "NO_PASSTHROUGH",
    "PASSTHROUGH",
]


# --- restJson1 ser/de ---
def serialize_json(value: M3u8TimedMetadataBehavior) -> str:
    return value


def deserialize_json(data: str) -> M3u8TimedMetadataBehavior:
    return cast(M3u8TimedMetadataBehavior, data)
