"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceGroupByField``."""

from typing import Literal, TypeAlias, cast

ResourceGroupByField: TypeAlias = Literal[
    "AccountId",
    "Region",
    "ResourceCategory",
    "ResourceType",
    "ResourceName",
    "FindingsSummary.FindingType",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroupByField) -> str:
    return value


def deserialize_json(data: str) -> ResourceGroupByField:
    return cast(ResourceGroupByField, data)
