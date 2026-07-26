"""Generated from Smithy shape ``com.amazonaws.auditmanager#StartAssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_auditmanager.types.account_id
    import capo_auditmanager.types.region
    import capo_auditmanager.types.share_request_comment
    import capo_auditmanager.types.uuid


class StartAssessmentFrameworkShareRequest(TypedDict, closed=True):
    framework_id: "capo_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the custom framework to be shared. </p>"""
    destination_account: "capo_auditmanager.types.account_id.AccountId"
    """<p> The Amazon Web Services account of the recipient. </p>"""
    destination_region: "capo_auditmanager.types.region.Region"
    """<p> The Amazon Web Services Region of the recipient. </p>"""
    comment: NotRequired[
        "capo_auditmanager.types.share_request_comment.ShareRequestComment"
    ]
    """<p> An optional comment from the sender about the share request. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartAssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    out["destinationAccount"] = value["destination_account"]
    out["destinationRegion"] = value["destination_region"]
    if "comment" in value:
        out["comment"] = value["comment"]
    return out


def deserialize_json(data: dict) -> StartAssessmentFrameworkShareRequest:
    out: StartAssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    if "destinationAccount" in data:
        out["destination_account"] = data["destinationAccount"]
    else:
        raise DeserializationError(
            "StartAssessmentFrameworkShareRequest.destination_account required"
        )
    if "destinationRegion" in data:
        out["destination_region"] = data["destinationRegion"]
    else:
        raise DeserializationError(
            "StartAssessmentFrameworkShareRequest.destination_region required"
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    return out
