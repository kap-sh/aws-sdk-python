"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesDateField``."""

from typing import Literal, TypeAlias, cast

ResourcesDateField: TypeAlias = Literal[
    "ResourceDetailCaptureTime",
    "ResourceCreationTime",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesDateField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesDateField:
    return cast(ResourcesDateField, data)
