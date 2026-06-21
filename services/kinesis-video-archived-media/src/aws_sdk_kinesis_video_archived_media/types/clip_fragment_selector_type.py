"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#ClipFragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

ClipFragmentSelectorType: TypeAlias = Literal[
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: ClipFragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> ClipFragmentSelectorType:
    return cast(ClipFragmentSelectorType, data)
