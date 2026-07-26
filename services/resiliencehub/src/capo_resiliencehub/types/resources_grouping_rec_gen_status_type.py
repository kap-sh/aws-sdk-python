"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourcesGroupingRecGenStatusType``."""

from typing import Literal, TypeAlias, cast

ResourcesGroupingRecGenStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesGroupingRecGenStatusType) -> str:
    return value


def deserialize_json(data: str) -> ResourcesGroupingRecGenStatusType:
    return cast(ResourcesGroupingRecGenStatusType, data)
