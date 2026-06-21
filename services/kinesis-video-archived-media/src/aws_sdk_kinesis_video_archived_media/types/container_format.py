"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ContainerFormat``."""

from typing import Literal, TypeAlias, cast

ContainerFormat: TypeAlias = Literal[
    "FRAGMENTED_MP4",
    "MPEG_TS",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContainerFormat) -> str:
    return value


def deserialize_json(data: str) -> ContainerFormat:
    return cast(ContainerFormat, data)
