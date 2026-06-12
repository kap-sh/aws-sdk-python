"""Generated from Smithy shape ``com.amazonaws.connect#HierarchyLevelUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_connect.types.hierarchy_level_name


class HierarchyLevelUpdate(TypedDict):
    name: "aws_sdk_connect.types.hierarchy_level_name.HierarchyLevelName"
    """<p>The name of the user hierarchy level. Must not be more than 50 characters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HierarchyLevelUpdate) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> HierarchyLevelUpdate:
    out: HierarchyLevelUpdate = {}  # type: ignore[typeddict-item]
    if "Name" in data:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("HierarchyLevelUpdate.name required")
    return out
