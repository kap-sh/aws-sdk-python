"""Generated from Smithy shape ``com.amazonaws.mediaconvert#VchipAction``."""

from typing import Literal, TypeAlias, cast

"""The action to take on content advisory XDS packets. If you select PASSTHROUGH, packets will not be changed. If you select STRIP, any packets will be removed in output captions."""
VchipAction: TypeAlias = Literal[
    "PASSTHROUGH",
    "STRIP",
]


# --- restJson1 ser/de ---
def serialize_json(value: VchipAction) -> str:
    return value


def deserialize_json(data: str) -> VchipAction:
    return cast(VchipAction, data)
