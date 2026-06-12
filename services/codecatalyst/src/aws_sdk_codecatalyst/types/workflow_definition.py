"""Generated from Smithy shape ``com.amazonaws.codecatalyst#WorkflowDefinition``."""

from typing import TypedDict

from aws_sdk_codecatalyst.errors import DeserializationError


class WorkflowDefinition(TypedDict):
    path: "str"
    """<p>The path to the workflow definition file stored in the source repository for the project, including the file name.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowDefinition) -> dict:
    out: dict = {}
    out["path"] = value["path"]
    return out


def deserialize_json(data: dict) -> WorkflowDefinition:
    out: WorkflowDefinition = {}  # type: ignore[typeddict-item]
    if "path" in data:
        out["path"] = data["path"]
    else:
        raise DeserializationError("WorkflowDefinition.path required")
    return out
