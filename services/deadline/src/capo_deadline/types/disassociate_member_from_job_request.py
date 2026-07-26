"""Generated from Smithy shape ``com.amazonaws.deadline#DisassociateMemberFromJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.farm_id
    import capo_deadline.types.identity_center_principal_id
    import capo_deadline.types.job_id
    import capo_deadline.types.queue_id


class DisassociateMemberFromJobRequest(TypedDict, closed=True):
    farm_id: "capo_deadline.types.farm_id.FarmId"
    """<p>The farm ID for the job to disassociate from the member.</p>"""
    queue_id: "capo_deadline.types.queue_id.QueueId"
    """<p>The queue ID connected to a job for which you're disassociating a member.</p>"""
    job_id: "capo_deadline.types.job_id.JobId"
    """<p>The job ID to disassociate from a member in a job.</p>"""
    principal_id: (
        "capo_deadline.types.identity_center_principal_id.IdentityCenterPrincipalId"
    )
    """<p>A member's principal ID to disassociate from a job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateMemberFromJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateMemberFromJobRequest:
    out: DisassociateMemberFromJobRequest = {}  # type: ignore[typeddict-item]
    return out
