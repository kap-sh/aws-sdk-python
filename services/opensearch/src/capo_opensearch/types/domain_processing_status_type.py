"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainProcessingStatusType``."""

from typing import Literal, TypeAlias, cast

DomainProcessingStatusType: TypeAlias = Literal[
    "Creating",
    "Active",
    "Modifying",
    "UpgradingEngineVersion",
    "UpdatingServiceSoftware",
    "Isolated",
    "Deleting",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainProcessingStatusType) -> str:
    return value


def deserialize_json(data: str) -> DomainProcessingStatusType:
    return cast(DomainProcessingStatusType, data)
