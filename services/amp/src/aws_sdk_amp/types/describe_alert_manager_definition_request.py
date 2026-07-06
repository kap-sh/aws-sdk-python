"""Generated from Smithy shape ``com.amazonaws.amp#DescribeAlertManagerDefinitionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_amp.types.workspace_id


class DescribeAlertManagerDefinitionRequest(TypedDict, closed=True):
    workspace_id: "aws_sdk_amp.types.workspace_id.WorkspaceId"
    """<p>The ID of the workspace to retrieve the alert manager definition from.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeAlertManagerDefinitionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeAlertManagerDefinitionRequest:
    out: DescribeAlertManagerDefinitionRequest = {}  # type: ignore[typeddict-item]
    return out
