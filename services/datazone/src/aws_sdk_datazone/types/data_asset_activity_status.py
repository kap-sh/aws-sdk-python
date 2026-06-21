"""Generated from Smithy shape ``com.amazonaws.datazone#DataAssetActivityStatus``."""

from typing import Literal, TypeAlias, cast

DataAssetActivityStatus: TypeAlias = Literal[
    "FAILED",
    "PUBLISHING_FAILED",
    "SUCCEEDED_CREATED",
    "SUCCEEDED_UPDATED",
    "SKIPPED_ALREADY_IMPORTED",
    "SKIPPED_ARCHIVED",
    "SKIPPED_NO_ACCESS",
    "UNCHANGED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAssetActivityStatus) -> str:
    return value


def deserialize_json(data: str) -> DataAssetActivityStatus:
    return cast(DataAssetActivityStatus, data)
