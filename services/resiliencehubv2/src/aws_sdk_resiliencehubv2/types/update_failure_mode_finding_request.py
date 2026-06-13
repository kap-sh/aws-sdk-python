"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#UpdateFailureModeFindingRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehubv2.types.arn
    import aws_sdk_resiliencehubv2.types.finding_status
    import aws_sdk_resiliencehubv2.types.uuid


class UpdateFailureModeFindingRequest(TypedDict):
    finding_id: "aws_sdk_resiliencehubv2.types.uuid.Uuid"
    """<p>The identifier of the finding to update.</p>"""
    status: "aws_sdk_resiliencehubv2.types.finding_status.FindingStatus"
    """<p>The new status for the finding.</p>"""
    service_arn: "aws_sdk_resiliencehubv2.types.arn.Arn"
    comment: NotRequired["str"]
    """<p>A comment about the finding update.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateFailureModeFindingRequest) -> dict:
    out: dict = {}
    out["findingId"] = value["finding_id"]
    import aws_sdk_resiliencehubv2.types.finding_status

    out["status"] = aws_sdk_resiliencehubv2.types.finding_status.serialize_json(
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
        import aws_sdk_resiliencehubv2.types.finding_status

        out["status"] = aws_sdk_resiliencehubv2.types.finding_status.deserialize_json(
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
