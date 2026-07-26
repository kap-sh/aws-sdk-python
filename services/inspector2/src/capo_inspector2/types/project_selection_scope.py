"""Generated from Smithy shape ``com.amazonaws.inspector2#ProjectSelectionScope``."""

from typing import Literal, TypeAlias, cast

ProjectSelectionScope: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: ProjectSelectionScope) -> str:
    return value


def deserialize_json(data: str) -> ProjectSelectionScope:
    return cast(ProjectSelectionScope, data)
