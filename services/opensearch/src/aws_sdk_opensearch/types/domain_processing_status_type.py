"""Generated from Smithy shape ``com.amazonaws.opensearch#DomainProcessingStatusType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_opensearch.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
        "Creating",
        "Active",
        "Modifying",
        "UpgradingEngineVersion",
        "UpdatingServiceSoftware",
        "Isolated",
        "Deleting",
    )
)


def serialize_json(value: DomainProcessingStatusType) -> str:
    return value


def deserialize_json(data: str) -> DomainProcessingStatusType:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown DomainProcessingStatusType value: {data!r}"
        )
    return cast(DomainProcessingStatusType, data)
