"""Generated from Smithy shape ``com.amazonaws.medialive#NielsenWatermarksDistributionTypes``."""

from typing import Literal, TypeAlias, cast

"""Nielsen Watermarks Distribution Types"""
NielsenWatermarksDistributionTypes: TypeAlias = Literal[
    "FINAL_DISTRIBUTOR",
    "PROGRAM_CONTENT",
]


# --- restJson1 ser/de ---
def serialize_json(value: NielsenWatermarksDistributionTypes) -> str:
    return value


def deserialize_json(data: str) -> NielsenWatermarksDistributionTypes:
    return cast(NielsenWatermarksDistributionTypes, data)
