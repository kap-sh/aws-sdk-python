"""Generated from Smithy shape ``com.amazonaws.securityir#InvestigationAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_security_ir.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_security_ir.types.action_type
    import aws_sdk_security_ir.types.execution_status
    import aws_sdk_security_ir.types.investigation_content
    import aws_sdk_security_ir.types.investigation_feedback
    import aws_sdk_security_ir.types.investigation_id
    import aws_sdk_security_ir.types.investigation_title


class InvestigationAction(TypedDict):
    investigation_id: "aws_sdk_security_ir.types.investigation_id.InvestigationId"
    """<p>The unique identifier for this investigation action. This ID is used to track and reference the specific investigation throughout its lifecycle.</p>"""
    action_type: "aws_sdk_security_ir.types.action_type.ActionType"
    """<p>The type of investigation action being performed. This categorizes the investigation method or approach used in the case.</p>"""
    title: "aws_sdk_security_ir.types.investigation_title.InvestigationTitle"
    """<p>Human-readable summary of the investigation focus. This provides a brief description of what the investigation is examining or analyzing.</p>"""
    content: "aws_sdk_security_ir.types.investigation_content.InvestigationContent"
    """<p>Detailed investigation results in rich markdown format. This field contains the comprehensive findings, analysis, and conclusions from the investigation.</p>"""
    status: "aws_sdk_security_ir.types.execution_status.ExecutionStatus"
    """<p>The current execution status of the investigation. This indicates whether the investigation is pending, in progress, completed, or failed.</p>"""
    last_updated: "datetime.datetime"
    """<p>ISO 8601 timestamp of the most recent status update. This indicates when the investigation was last modified or when its status last changed.</p>"""
    feedback: NotRequired[
        "aws_sdk_security_ir.types.investigation_feedback.InvestigationFeedback"
    ]
    """<p>User feedback for this investigation result. This contains the user's assessment and comments about the quality and usefulness of the investigation findings.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvestigationAction) -> dict:
    out: dict = {}
    out["investigationId"] = value["investigation_id"]
    import aws_sdk_security_ir.types.action_type

    out["actionType"] = aws_sdk_security_ir.types.action_type.serialize_json(
        value["action_type"]
    )
    out["title"] = value["title"]
    out["content"] = value["content"]
    import aws_sdk_security_ir.types.execution_status

    out["status"] = aws_sdk_security_ir.types.execution_status.serialize_json(
        value["status"]
    )
    import aws_sdk_security_ir.types._prelude.timestamp

    out["lastUpdated"] = aws_sdk_security_ir.types._prelude.timestamp.serialize_json(
        value["last_updated"]
    )
    if "feedback" in value:
        import aws_sdk_security_ir.types.investigation_feedback

        out["feedback"] = (
            aws_sdk_security_ir.types.investigation_feedback.serialize_json(
                value["feedback"]
            )
        )
    return out


def deserialize_json(data: dict) -> InvestigationAction:
    out: InvestigationAction = {}  # type: ignore[typeddict-item]
    if "investigationId" in data:
        out["investigation_id"] = data["investigationId"]
    else:
        raise DeserializationError("InvestigationAction.investigation_id required")
    if "actionType" in data:
        import aws_sdk_security_ir.types.action_type

        out["action_type"] = aws_sdk_security_ir.types.action_type.deserialize_json(
            data["actionType"]
        )
    else:
        raise DeserializationError("InvestigationAction.action_type required")
    if "title" in data:
        out["title"] = data["title"]
    else:
        raise DeserializationError("InvestigationAction.title required")
    if "content" in data:
        out["content"] = data["content"]
    else:
        raise DeserializationError("InvestigationAction.content required")
    if "status" in data:
        import aws_sdk_security_ir.types.execution_status

        out["status"] = aws_sdk_security_ir.types.execution_status.deserialize_json(
            data["status"]
        )
    else:
        raise DeserializationError("InvestigationAction.status required")
    if "lastUpdated" in data:
        import aws_sdk_security_ir.types._prelude.timestamp

        out["last_updated"] = (
            aws_sdk_security_ir.types._prelude.timestamp.deserialize_json(
                data["lastUpdated"]
            )
        )
    else:
        raise DeserializationError("InvestigationAction.last_updated required")
    if "feedback" in data:
        import aws_sdk_security_ir.types.investigation_feedback

        out["feedback"] = (
            aws_sdk_security_ir.types.investigation_feedback.deserialize_json(
                data["feedback"]
            )
        )
    return out
