"""Generated from Smithy shape ``com.amazonaws.deadline#SyncInputJobAttachmentsSessionActionDefinition``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_id


class SyncInputJobAttachmentsSessionActionDefinition(TypedDict):
    step_id: NotRequired["aws_sdk_deadline.types.step_id.StepId"]
    """<p>The step ID for the sync input job attachments session action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SyncInputJobAttachmentsSessionActionDefinition) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    return out


def deserialize_json(data: dict) -> SyncInputJobAttachmentsSessionActionDefinition:
    out: SyncInputJobAttachmentsSessionActionDefinition = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    return out
