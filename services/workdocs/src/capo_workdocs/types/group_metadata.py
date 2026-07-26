"""Generated from Smithy shape ``com.amazonaws.workdocs#GroupMetadata``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workdocs.types.group_name_type
    import capo_workdocs.types.id_type


class GroupMetadata(TypedDict, closed=True):
    id: NotRequired["capo_workdocs.types.id_type.IdType"]
    """<p>The ID of the user group.</p>"""
    name: NotRequired["capo_workdocs.types.group_name_type.GroupNameType"]
    """<p>The name of the group.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GroupMetadata) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> GroupMetadata:
    out: GroupMetadata = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
