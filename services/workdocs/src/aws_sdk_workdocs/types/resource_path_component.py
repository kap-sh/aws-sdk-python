"""Generated from Smithy shape ``com.amazonaws.workdocs#ResourcePathComponent``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_workdocs.types.id_type
    import aws_sdk_workdocs.types.resource_name_type


class ResourcePathComponent(TypedDict, closed=True):
    id: NotRequired["aws_sdk_workdocs.types.id_type.IdType"]
    """<p>The ID of the resource path.</p>"""
    name: NotRequired["aws_sdk_workdocs.types.resource_name_type.ResourceNameType"]
    """<p>The name of the resource path.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ResourcePathComponent) -> dict:
    out: dict = {}
    if "id" in value:
        out["Id"] = value["id"]
    if "name" in value:
        out["Name"] = value["name"]
    return out


def deserialize_json(data: dict) -> ResourcePathComponent:
    out: ResourcePathComponent = {}  # type: ignore[typeddict-item]
    if "Id" in data:
        out["id"] = data["Id"]
    if "Name" in data:
        out["name"] = data["Name"]
    return out
