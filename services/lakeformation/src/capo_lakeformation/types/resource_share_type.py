"""Generated from Smithy shape ``com.amazonaws.lakeformation#ResourceShareType``."""

from typing import Literal, TypeAlias, cast

ResourceShareType: TypeAlias = Literal[
    "FOREIGN",
    "ALL",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceShareType) -> str:
    return value


def deserialize_json(data: str) -> ResourceShareType:
    return cast(ResourceShareType, data)
