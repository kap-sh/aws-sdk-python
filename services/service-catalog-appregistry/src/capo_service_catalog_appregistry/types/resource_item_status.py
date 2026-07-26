"""Generated from Smithy shape ``com.amazonaws.servicecatalogappregistry#ResourceItemStatus``."""

from typing import Literal, TypeAlias, cast

ResourceItemStatus: TypeAlias = Literal[
    "SUCCESS",
    "FAILED",
    "IN_PROGRESS",
    "SKIPPED",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceItemStatus) -> str:
    return value


def deserialize_json(data: str) -> ResourceItemStatus:
    return cast(ResourceItemStatus, data)
