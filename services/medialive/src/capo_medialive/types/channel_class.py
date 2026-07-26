"""Generated from Smithy shape ``com.amazonaws.medialive#ChannelClass``."""

from typing import Literal, TypeAlias, cast

"""A standard channel has two encoding pipelines and a single pipeline channel only has one."""
ChannelClass: TypeAlias = Literal[
    "STANDARD",
    "SINGLE_PIPELINE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ChannelClass) -> str:
    return value


def deserialize_json(data: str) -> ChannelClass:
    return cast(ChannelClass, data)
