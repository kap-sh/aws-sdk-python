"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentFrameworkShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_auditmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.share_request_action
    import aws_sdk_auditmanager.types.share_request_type
    import aws_sdk_auditmanager.types.uuid


class UpdateAssessmentFrameworkShareRequest(TypedDict, closed=True):
    request_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the share request. </p>"""
    request_type: "aws_sdk_auditmanager.types.share_request_type.ShareRequestType"
    """<p>Specifies whether the share request is a sent request or a received request.</p>"""
    action: "aws_sdk_auditmanager.types.share_request_action.ShareRequestAction"
    """<p>Specifies the update action for the share request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentFrameworkShareRequest) -> dict:
    out: dict = {}
    import aws_sdk_auditmanager.types.share_request_type

    out["requestType"] = aws_sdk_auditmanager.types.share_request_type.serialize_json(
        value["request_type"]
    )
    import aws_sdk_auditmanager.types.share_request_action

    out["action"] = aws_sdk_auditmanager.types.share_request_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateAssessmentFrameworkShareRequest:
    out: UpdateAssessmentFrameworkShareRequest = {}  # type: ignore[typeddict-item]
    if "requestType" in data:
        import aws_sdk_auditmanager.types.share_request_type

        out["request_type"] = (
            aws_sdk_auditmanager.types.share_request_type.deserialize_json(
                data["requestType"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentFrameworkShareRequest.request_type required"
        )
    if "action" in data:
        import aws_sdk_auditmanager.types.share_request_action

        out["action"] = (
            aws_sdk_auditmanager.types.share_request_action.deserialize_json(
                data["action"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateAssessmentFrameworkShareRequest.action required"
        )
    return out
