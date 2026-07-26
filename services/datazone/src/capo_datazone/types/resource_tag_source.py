"""Generated from Smithy shape ``com.amazonaws.datazone#ResourceTagSource``."""

from typing import Literal, TypeAlias, cast

ResourceTagSource: TypeAlias = Literal[
    "PROJECT",
    "PROJECT_PROFILE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceTagSource) -> str:
    return value


def deserialize_json(data: str) -> ResourceTagSource:
    return cast(ResourceTagSource, data)
