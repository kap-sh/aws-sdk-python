"""Generated from Smithy shape ``com.amazonaws.codecatalyst#StartWorkflowRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_codecatalyst.types.name_string
    import aws_sdk_codecatalyst.types.uuid


class StartWorkflowRunRequest(TypedDict, closed=True):
    space_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the space.</p>"""
    project_name: "aws_sdk_codecatalyst.types.name_string.NameString"
    """<p>The name of the project in the space.</p>"""
    workflow_id: "aws_sdk_codecatalyst.types.uuid.Uuid"
    """<p>The system-generated unique ID of the workflow. To retrieve a list of workflow IDs, use <a>ListWorkflows</a>.</p>"""
    client_token: NotRequired["str"]
    """<p>A user-specified idempotency token. Idempotency ensures that an API request completes only once. With an idempotent request, if the original request completes successfully, the subsequent retries return the result from the original successful request and have no additional effect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartWorkflowRunRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartWorkflowRunRequest:
    out: StartWorkflowRunRequest = {}  # type: ignore[typeddict-item]
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
