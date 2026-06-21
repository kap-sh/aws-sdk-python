"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightSearchFilterName``."""

from typing import Literal, TypeAlias, cast

SpaceQuickSightSearchFilterName: TypeAlias = Literal[
    "SPACE_ID",
    "SPACE_NAME",
    "DIRECT_QUICKSIGHT_OWNER",
    "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
    "DIRECT_QUICKSIGHT_SOLE_OWNER",
    "CONTRIBUTED_BY",
    "CONSUMED_SOURCE_SIZE",
    "CREATED_BY",
]


# --- restJson1 ser/de ---
def serialize_json(value: SpaceQuickSightSearchFilterName) -> str:
    return value


def deserialize_json(data: str) -> SpaceQuickSightSearchFilterName:
    return cast(SpaceQuickSightSearchFilterName, data)
