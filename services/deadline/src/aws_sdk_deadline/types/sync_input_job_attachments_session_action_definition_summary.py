"""Generated from Smithy shape ``com.amazonaws.deadline#SyncInputJobAttachmentsSessionActionDefinitionSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_deadline.types.step_id


class SyncInputJobAttachmentsSessionActionDefinitionSummary(TypedDict):
    step_id: NotRequired["aws_sdk_deadline.types.step_id.StepId"]
    """<p>The step ID for the sync input job attachments session action summary.</p>"""


# --- restJson1 ser/de ---
def serialize_json(
    value: SyncInputJobAttachmentsSessionActionDefinitionSummary,
) -> dict:
    out: dict = {}
    if "step_id" in value:
        out["stepId"] = value["step_id"]
    return out


def deserialize_json(
    data: dict,
) -> SyncInputJobAttachmentsSessionActionDefinitionSummary:
    out: SyncInputJobAttachmentsSessionActionDefinitionSummary = {}  # type: ignore[typeddict-item]
    if "stepId" in data:
        out["step_id"] = data["stepId"]
    return out
