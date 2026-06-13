"""Generated from Smithy shape ``com.amazonaws.qconnect#PutFeedbackResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qconnect.types.content_feedback_data
    import aws_sdk_qconnect.types.target_type
    import aws_sdk_qconnect.types.uuid
    import aws_sdk_qconnect.types.uuid_or_arn


class PutFeedbackResponse(TypedDict):
    assistant_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the Amazon Q in Connect assistant.</p>"""
    assistant_arn: "aws_sdk_qconnect.types.uuid_or_arn.UuidOrArn"
    """<p>The Amazon Resource Name (ARN) of the Amazon Q in Connect assistant.</p>"""
    target_id: "aws_sdk_qconnect.types.uuid.Uuid"
    """<p>The identifier of the feedback target.</p>"""
    target_type: "aws_sdk_qconnect.types.target_type.TargetType"
    """<p>The type of the feedback target.</p>"""
    content_feedback: "aws_sdk_qconnect.types.content_feedback_data.ContentFeedbackData"
    """<p>Information about the feedback provided.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutFeedbackResponse) -> dict:
    out: dict = {}
    out["assistantId"] = value["assistant_id"]
    out["assistantArn"] = value["assistant_arn"]
    out["targetId"] = value["target_id"]
    out["targetType"] = value["target_type"]
    import aws_sdk_qconnect.types.content_feedback_data

    out["contentFeedback"] = (
        aws_sdk_qconnect.types.content_feedback_data.serialize_json(
            value["content_feedback"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutFeedbackResponse:
    out: PutFeedbackResponse = {}  # type: ignore[typeddict-item]
    if "assistantId" in data:
        out["assistant_id"] = data["assistantId"]
    else:
        raise DeserializationError("PutFeedbackResponse.assistant_id required")
    if "assistantArn" in data:
        out["assistant_arn"] = data["assistantArn"]
    else:
        raise DeserializationError("PutFeedbackResponse.assistant_arn required")
    if "targetId" in data:
        out["target_id"] = data["targetId"]
    else:
        raise DeserializationError("PutFeedbackResponse.target_id required")
    if "targetType" in data:
        out["target_type"] = data["targetType"]
    else:
        raise DeserializationError("PutFeedbackResponse.target_type required")
    if "contentFeedback" in data:
        import aws_sdk_qconnect.types.content_feedback_data

        out["content_feedback"] = (
            aws_sdk_qconnect.types.content_feedback_data.deserialize_json(
                data["contentFeedback"]
            )
        )
    else:
        raise DeserializationError("PutFeedbackResponse.content_feedback required")
    return out
