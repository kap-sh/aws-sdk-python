"""Generated from Smithy shape ``com.amazonaws.dlm#ResourceTypeValues``."""

from typing import Literal, TypeAlias, cast

ResourceTypeValues: TypeAlias = Literal[
    "VOLUME",
    "INSTANCE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTypeValues) -> str:
    return value


def deserialize_json(data: str) -> ResourceTypeValues:
    return cast(ResourceTypeValues, data)
