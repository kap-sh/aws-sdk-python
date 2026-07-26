"""Generated from Smithy shape ``com.amazonaws.wellarchitected#ShareResourceType``."""

from typing import Literal, TypeAlias, cast

ShareResourceType: TypeAlias = Literal[
    "WORKLOAD",
    "LENS",
    "PROFILE",
    "TEMPLATE",
]


# --- restJson1 ser/de ---
def serialize_json(value: ShareResourceType) -> str:
    return value


def deserialize_json(data: str) -> ShareResourceType:
    return cast(ShareResourceType, data)
