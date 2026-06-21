"""Generated from Smithy shape ``com.amazonaws.kinesisvideoarchivedmedia#DASHFragmentSelectorType``."""

from typing import Literal, TypeAlias, cast

DASHFragmentSelectorType: TypeAlias = Literal[
    "PRODUCER_TIMESTAMP",
    "SERVER_TIMESTAMP",
]


# --- restJson1 ser/de ---
def serialize_json(value: DASHFragmentSelectorType) -> str:
    return value


def deserialize_json(data: str) -> DASHFragmentSelectorType:
    return cast(DASHFragmentSelectorType, data)
