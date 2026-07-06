"""Generated from Smithy shape ``com.amazonaws.imagebuilder#WorkflowState``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_imagebuilder.types.non_empty_string
    import aws_sdk_imagebuilder.types.workflow_status


class WorkflowState(TypedDict, closed=True):
    status: NotRequired["aws_sdk_imagebuilder.types.workflow_status.WorkflowStatus"]
    """<p>The current state of the workflow.</p>"""
    reason: NotRequired["aws_sdk_imagebuilder.types.non_empty_string.NonEmptyString"]
    """<p>Describes how or why the workflow changed state.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WorkflowState) -> dict:
    out: dict = {}
    if "status" in value:
        import aws_sdk_imagebuilder.types.workflow_status

        out["status"] = aws_sdk_imagebuilder.types.workflow_status.serialize_json(
            value["status"]
        )
    if "reason" in value:
        out["reason"] = value["reason"]
    return out


def deserialize_json(data: dict) -> WorkflowState:
    out: WorkflowState = {}  # type: ignore[typeddict-item]
    if "status" in data:
        import aws_sdk_imagebuilder.types.workflow_status

        out["status"] = aws_sdk_imagebuilder.types.workflow_status.deserialize_json(
            data["status"]
        )
    if "reason" in data:
        out["reason"] = data["reason"]
    return out
