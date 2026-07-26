"""Generated from Smithy shape ``com.amazonaws.appsync#SourceApiAssociationStatus``."""

from typing import Literal, TypeAlias, cast

SourceApiAssociationStatus: TypeAlias = Literal[
    "MERGE_SCHEDULED",
    "MERGE_FAILED",
    "MERGE_SUCCESS",
    "MERGE_IN_PROGRESS",
    "AUTO_MERGE_SCHEDULE_FAILED",
    "DELETION_SCHEDULED",
    "DELETION_IN_PROGRESS",
    "DELETION_FAILED",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceApiAssociationStatus) -> str:
    return value


def deserialize_json(data: str) -> SourceApiAssociationStatus:
    return cast(SourceApiAssociationStatus, data)
