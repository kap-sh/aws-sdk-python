"""Generated from Smithy shape ``com.amazonaws.qconnect#PutFeedbackRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.content_feedback_data
    import aws_sdk_qconnect.types.target_type
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.uuid_or_arn


class PutFeedbackRequest(TypedDict, closed=True):
    assistant_id: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    target_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the feedback target.</p>"""
    target_type: "aws_sdk_qconnect.types.target_type.TargetType"
    """<p>The type of the feedback target.</p>"""
    content_feedback: "aws_sdk_qconnect.types.content_feedback_data.ContentFeedbackData"
    """<p>Information about the feedback provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFeedbackRequest) -> dict:
    out: dict = {}
    out["targetId"] = value["target_id"]
    out["targetType"] = value["target_type"]
    import aws_sdk_qconnect.types.content_feedback_data

    out["contentFeedback"] = (
        aws_sdk_qconnect.types.content_feedback_data.serialize_json(
            value["content_feedback"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutFeedbackRequest:
    out: PutFeedbackRequest = {}  # type: ignore[typeddict-item]
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("PutFeedbackRequest.target_id required")
    if "targetType" in data:
        out["target_type"] = data["targetType"]
    else:
        raise DeserializationError("PutFeedbackRequest.target_type required")
    if "contentFeedback" in data:
        import aws_sdk_qconnect.types.content_feedback_data

        out["content_feedback"] = (
            aws_sdk_qconnect.types.content_feedback_data.deserialize_json(
                data["contentFeedback"]
            )
        )
    else:
        raise DeserializationError("PutFeedbackRequest.content_feedback required")
    return out
