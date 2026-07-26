"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetSqsQueueParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.message_deduplication_id
    import capo_pipes.types.message_group_id


class PipeTargetSqsQueueParameters(TypedDict, closed=True):
    message_group_id: NotRequired["capo_pipes.types.message_group_id.MessageGroupId"]
    """<p>The FIFO message group ID to use as the target.</p>"""
    message_deduplication_id: NotRequired[
        "capo_pipes.types.message_deduplication_id.MessageDeduplicationId"
    ]
    """<p>This parameter applies only to FIFO (first-in-first-out) queues.</p> <p>The token used for deduplication of sent messages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetSqsQueueParameters) -> dict:
    out: dict = {}
    if "message_group_id" in value:
        out["MessageGroupId"] = value["message_group_id"]
    if "message_deduplication_id" in value:
        out["MessageDeduplicationId"] = value["message_deduplication_id"]
    return out


def deserialize_json(data: dict) -> PipeTargetSqsQueueParameters:
    out: PipeTargetSqsQueueParameters = {}  # type: ignore[typeddict-item]
    if "MessageGroupId" in data:
        out["message_group_id"] = data["MessageGroupId"]
    if "MessageDeduplicationId" in data:
        out["message_deduplication_id"] = data["MessageDeduplicationId"]
    return out
