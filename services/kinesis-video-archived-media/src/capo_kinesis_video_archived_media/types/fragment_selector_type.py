"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#FragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

FragmentSelectorType: TypeAlias = Literal[
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: FragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> FragmentSelectorType:
    return cast(FragmentSelectorType, data)
