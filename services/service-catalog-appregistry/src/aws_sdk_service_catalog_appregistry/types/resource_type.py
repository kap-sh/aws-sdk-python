"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "CFN_STACK",
    "RESOURCE_TAG_VALUE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceType) -> str:
    return value


def deserialize_json(data: str) -> ResourceType:
    return cast(ResourceType, data)
