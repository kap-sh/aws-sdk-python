"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceQuickSightSearchFilterName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_quicksight.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "SPACE_ID",
        "SPACE_NAME",
        "DIRECT_QUICKSIGHT_OWNER",
        "DIRECT_QUICKSIGHT_VIEWER_OR_OWNER",
        "DIRECT_QUICKSIGHT_SOLE_OWNER",
        "CONTRIBUTED_BY",
        "CONSUMED_SOURCE_SIZE",
        "CREATED_BY",
    )
)


def serialize_json(value: SpaceQuickSightSearchFilterName) -> str:
    return value


def deserialize_json(data: str) -> SpaceQuickSightSearchFilterName:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown SpaceQuickSightSearchFilterName value: {data!r}"
        )
    return cast(SpaceQuickSightSearchFilterName, data)
