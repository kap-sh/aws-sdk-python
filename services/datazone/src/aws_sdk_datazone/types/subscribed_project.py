"""Generated from Smithy shape ``com.amazonaws.datazone#SubscribedProject``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.project_id
    import aws_sdk_datazone.types.project_name


class SubscribedProject(TypedDict):
    id: NotRequired["aws_sdk_datazone.types.project_id.ProjectId"]
    """<p>The identifier of the project that has the subscription grant.</p>"""
    name: NotRequired["aws_sdk_datazone.types.project_name.ProjectName"]
    """<p>The name of the project that has the subscription grant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SubscribedProject) -> dict:
    out: dict = {}
    if "id" in value:
        out["id"] = value["id"]
    if "name" in value:
        out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> SubscribedProject:
    out: SubscribedProject = {}  # type: ignore[typeddict-item]
    if "id" in data:
        out["id"] = data["id"]
    if "name" in data:
        out["name"] = data["name"]
    return out
