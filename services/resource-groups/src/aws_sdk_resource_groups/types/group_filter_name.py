"""Generated from Smithy shape ``com.amazonaws.resourcegroups#GroupFilterName``."""

from typing import Literal, TypeAlias, cast

GroupFilterName: TypeAlias = Literal[
    "resource-type",
    "configuration-type",
    "owner",
    "display-name",
    "criticality",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupFilterName) -> str:
    return value


def deserialize_json(data: str) -> GroupFilterName:
    return cast(GroupFilterName, data)
