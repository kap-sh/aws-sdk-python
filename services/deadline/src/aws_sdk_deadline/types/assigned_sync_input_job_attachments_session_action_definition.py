"""Generated from Smithy shape ``com.amazonaws.deadline#AssignedSyncInputJobAttachmentsSessionActionDefinition``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_id


class AssignedSyncInputJobAttachmentsSessionActionDefinition(TypedDict, closed=True):
    step_id: NotRequired["aws_sdk_deadline.types.step_id.StepId"]
    """<p>The step ID for the assigned sync input job attachments session action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: AssignedSyncInputJobAttachmentsSessionActionDefinition,
) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    return out


def deserialize_json(
    data: dict,
) -> AssignedSyncInputJobAttachmentsSessionActionDefinition:
    out: AssignedSyncInputJobAttachmentsSessionActionDefinition = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    return out
