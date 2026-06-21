"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#HLSFragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

HLSFragmentSelectorType: TypeAlias = Literal[
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: HLSFragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> HLSFragmentSelectorType:
    return cast(HLSFragmentSelectorType, data)
