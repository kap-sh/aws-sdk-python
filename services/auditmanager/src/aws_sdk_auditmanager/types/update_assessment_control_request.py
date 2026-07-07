"""Generated from Smithy shape ``com.amazonaws.auditmanager#UpdateAssessmentControlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_auditmanager.types.control_comment_body
    import aws_sdk_auditmanager.types.control_set_id
    import aws_sdk_auditmanager.types.control_status
    import aws_sdk_auditmanager.types.uuid


class UpdateAssessmentControlRequest(TypedDict, closed=True):
    assessment_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the assessment. </p>"""
    control_set_id: "aws_sdk_auditmanager.types.control_set_id.ControlSetId"
    """<p> The unique identifier for the control set. </p>"""
    control_id: "aws_sdk_auditmanager.types.uuid.UUID"
    """<p> The unique identifier for the control. </p>"""
    control_status: NotRequired[
        "aws_sdk_auditmanager.types.control_status.ControlStatus"
    ]
    """<p> The status of the control. </p>"""
    comment_body: NotRequired[
        "aws_sdk_auditmanager.types.control_comment_body.ControlCommentBody"
    ]
    """<p> The comment body text for the control. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateAssessmentControlRequest) -> dict:
    out: dict = {}
    if "control_status" in value:
        import aws_sdk_auditmanager.types.control_status

        out["controlStatus"] = aws_sdk_auditmanager.types.control_status.serialize_json(
            value["control_status"]
        )
    if "comment_body" in value:
        out["commentBody"] = value["comment_body"]
    return out


def deserialize_json(data: dict) -> UpdateAssessmentControlRequest:
    out: UpdateAssessmentControlRequest = {}  # type: ignore[typeddict-item]
    if "controlStatus" in data:
        import aws_sdk_auditmanager.types.control_status

        out["control_status"] = (
            aws_sdk_auditmanager.types.control_status.deserialize_json(
                data["controlStatus"]
            )
        )
    if "commentBody" in data:
        out["comment_body"] = data["commentBody"]
    return out
