"""Generated from Smithy shape ``com.amazonaws.appflow#PathPrefixHierarchy``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_appflow.types.path_prefix

PathPrefixHierarchy: TypeAlias = list["capo_appflow.types.path_prefix.PathPrefix"]


# --- restJson1 ser/de ---
def serialize_json(value: PathPrefixHierarchy) -> list:
    import capo_appflow.types.path_prefix

    out: list = []
    for item in value:
        out.append(capo_appflow.types.path_prefix.serialize_json(item))
    return out


def deserialize_json(data: list) -> PathPrefixHierarchy:
    import capo_appflow.types.path_prefix

    out: PathPrefixHierarchy = []
    for item in data:
        out.append(capo_appflow.types.path_prefix.deserialize_json(item))
    return out
