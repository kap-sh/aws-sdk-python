"""Generated from Smithy shape ``com.amazonaws.codeartifact#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "domain",
    "repository",
    "package",
    "package-version",
    "asset",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
