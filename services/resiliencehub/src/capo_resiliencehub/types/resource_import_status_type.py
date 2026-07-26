"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceImportStatusType``."""

from typing import Literal, TypeAlias, cast

ResourceImportStatusType: TypeAlias = Literal[
    "Pending",
    "InProgress",
    "Failed",
    "Success",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceImportStatusType) -> str:
    return value


def deserialize_json(data: str) -> ResourceImportStatusType:
    return cast(ResourceImportStatusType, data)
