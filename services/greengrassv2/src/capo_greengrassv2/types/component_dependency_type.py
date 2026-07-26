"""Generated from Smithy shape ``com.amazonaws.greengrassv2#ComponentDependencyType``."""

from typing import Literal, TypeAlias, cast

ComponentDependencyType: TypeAlias = Literal[
    "HARD",
    "SOFT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentDependencyType) -> str:
    return value


def deserialize_json(data: str) -> ComponentDependencyType:
    return cast(ComponentDependencyType, data)
