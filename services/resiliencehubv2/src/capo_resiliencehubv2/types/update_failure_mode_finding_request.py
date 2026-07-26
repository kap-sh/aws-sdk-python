"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateFailureModeFindingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.finding_status
    import capo_resiliencehubv2.types.uuid


class UpdateFailureModeFindingRequest(TypedDict, closed=True):
    finding_id: "capo_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the finding to update.</p>"""
    status: "capo_resiliencehubv2.types.finding_status.FindingStatus"
    """<p>The new status for the finding.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    comment: NotRequired["str"]
    """<p>A comment about the finding update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFailureModeFindingRequest) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import capo_resiliencehubv2.types.finding_status

    out["status"] = capo_resiliencehubv2.types.finding_status.serialize_json(
        value["status"]
    )
    out["serviceArn"] = value["service_arn"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> UpdateFailureModeFindingRequest:
    out: UpdateFailureModeFindingRequest = {}  # type: ignore[typeddict-item]
    if "findingId" in data:
        out["finding_id"] = data["findingId"]
    else:
        raise DeserializationError(
            "UpdateFailureModeFindingRequest.finding_id required"
        )
    if "status" in data:
        import capo_resiliencehubv2.types.finding_status

        out["status"] = capo_resiliencehubv2.types.finding_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("UpdateFailureModeFindingRequest.status required")
    if "serviceArn" in data:
        out["service_arn"] = data["serviceArn"]
    else:
        raise DeserializationError(
            "UpdateFailureModeFindingRequest.service_arn required"
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
