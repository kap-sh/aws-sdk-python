"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyGroupMatchType``."""

from typing import Literal, TypeAlias, cast

HierarchyGroupMatchType: TypeAlias = Literal[
    "EXACT",
    "WITH_CHILD_GROUPS",
]


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyGroupMatchType) -> str:
    return value


def deserialize_json(data: str) -> HierarchyGroupMatchType:
    return cast(HierarchyGroupMatchType, data)
