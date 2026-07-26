"""Generated from Smithy shape ``com.amazonaws.resourceexplorer2#CreateResourceExplorerSetupOutput``."""

from typing_extensions import TypedDict

from capo_resource_explorer_2.errors import DeserializationError


class CreateResourceExplorerSetupOutput(TypedDict, closed=True):
    task_id: "str"
    """<p>The unique identifier for the setup task. Use this ID with <code>GetResourceExplorerSetup</code> to monitor the progress of the configuration operation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateResourceExplorerSetupOutput) -> dict:
    out: dict = {}
    out["TaskId"] = value["task_id"]
    return out


def deserialize_json(data: dict) -> CreateResourceExplorerSetupOutput:
    out: CreateResourceExplorerSetupOutput = {}  # type: ignore[typeddict-item]
    if "TaskId" in data:
        out["task_id"] = data["TaskId"]
    else:
        raise DeserializationError("CreateResourceExplorerSetupOutput.task_id required")
    return out
