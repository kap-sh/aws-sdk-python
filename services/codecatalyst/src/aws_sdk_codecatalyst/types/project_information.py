"""Generated from Smithy shape ``com.amazonaws.codecatalyst#ProjectInformation``."""

from typing_extensions import NotRequired, TypedDict


class ProjectInformation(TypedDict, closed=True):
    name: NotRequired["str"]
    """<p>The name of the project in the space.</p>"""
    project_id: NotRequired["str"]
    """<p>The system-generated unique ID of the project.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProjectInformation) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "project_id" in value:
        out["projectId"] = value["project_id"]
    return out


def deserialize_json(data: dict) -> ProjectInformation:
    out: ProjectInformation = {}  # type: ignore[typeddict-item]
    if "name" in data:
        out["name"] = data["name"]
    if "projectId" in data:
        out["project_id"] = data["projectId"]
    return out
