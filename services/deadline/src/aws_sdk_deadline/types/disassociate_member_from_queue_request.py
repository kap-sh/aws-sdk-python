"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromQueueRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_deadline.types.farm_id
    import aws_sdk_deadline.types.identity_center_principal_id
    import aws_sdk_deadline.types.queue_id


class DisassociateMemberFromQueueRequest(TypedDict):
    farm_id: "aws_sdk_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the queue to disassociate from a member.</p>"""
    queue_id: "aws_sdk_deadline.types.queue_id.QueueId"
    """<p>The queue ID of the queue in which you're disassociating from a member.</p>"""
    principal_id: (
        "aws_sdk_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>A member's principal ID to disassociate from a queue.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromQueueRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromQueueRequest:
    out: DisassociateMemberFromQueueRequest = {}  # type: ignore[typeddict-item]
    return out
