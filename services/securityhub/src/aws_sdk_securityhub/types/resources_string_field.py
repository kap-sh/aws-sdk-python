"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesStringField``."""

from typing import Literal, TypeAlias, cast

ResourcesStringField: TypeAlias = Literal[
    "ResourceGuid",
    "ResourceId",
    "AccountId",
    "Region",
    "ResourceCategory",
    "ResourceType",
    "ResourceName",
    "FindingsSummary.FindingType",
    "FindingsSummary.ProductName",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesStringField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesStringField:
    return cast(ResourcesStringField, data)
