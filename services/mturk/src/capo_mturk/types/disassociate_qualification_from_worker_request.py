"""Generated from Smithy shape ``com.amazonaws.mturk#DisassociateQualificationFromWorkerRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mturk.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mturk.types.customer_id
    import capo_mturk.types.entity_id
    import capo_mturk.types.string


class DisassociateQualificationFromWorkerRequest(TypedDict, closed=True):
    worker_id: "capo_mturk.types.customer_id.CustomerId"
    """<p>The ID of the Worker who possesses the Qualification to be revoked.</p>"""
    qualification_type_id: "capo_mturk.types.entity_id.EntityId"
    """<p>The ID of the Qualification type of the Qualification to be revoked.</p>"""
    reason: NotRequired["capo_mturk.types.string.String"]
    """<p>A text message that explains why the Qualification was revoked. The user who had the Qualification sees this message.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DisassociateQualificationFromWorkerRequest) -> dict:
    out: dict = {}
    out["WorkerId"] = value["worker_id"]
    out["QualificationTypeId"] = value["qualification_type_id"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DisassociateQualificationFromWorkerRequest:
    out: DisassociateQualificationFromWorkerRequest = {}  # type: ignore[typeddict-item]
    if "WorkerId" in data:
        out["worker_id"] = data["WorkerId"]
    else:
        raise DeserializationError(
            "DisassociateQualificationFromWorkerRequest.worker_id required"
        )
    if "QualificationTypeId" in data:
        out["qualification_type_id"] = data["QualificationTypeId"]
    else:
        raise DeserializationError(
            "DisassociateQualificationFromWorkerRequest.qualification_type_id required"
        )
    if "Reason" in data:
        out["reason"] = data["Reason"]
    return out
