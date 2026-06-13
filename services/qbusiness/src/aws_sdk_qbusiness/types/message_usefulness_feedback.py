"""Generated from Smithy shape ``com.amazonaws.qbusiness#MessageUsefulnessFeedback``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_qbusiness.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.message_usefulness
    import aws_sdk_qbusiness.types.message_usefulness_comment
    import aws_sdk_qbusiness.types.message_usefulness_reason
    import aws_sdk_qbusiness.types.timestamp


class MessageUsefulnessFeedback(TypedDict):
    usefulness: "aws_sdk_qbusiness.types.message_usefulness.MessageUsefulness"
    """<p>The usefulness value assigned by an end user to a message.</p>"""
    reason: NotRequired[
        "aws_sdk_qbusiness.types.message_usefulness_reason.MessageUsefulnessReason"
    ]
    """<p>The reason for a usefulness rating.</p>"""
    comment: NotRequired[
        "aws_sdk_qbusiness.types.message_usefulness_comment.MessageUsefulnessComment"
    ]
    """<p>A comment given by an end user on the usefulness of an AI-generated chat message.</p>"""
    submitted_at: "aws_sdk_qbusiness.types.timestamp.Timestamp"
    """<p>The timestamp for when the feedback was submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MessageUsefulnessFeedback) -> dict:
    out: dict = {}
    import aws_sdk_qbusiness.types.message_usefulness

    out["usefulness"] = aws_sdk_qbusiness.types.message_usefulness.serialize_json(
        value["usefulness"]
    )
    if "reason" in value:
        import aws_sdk_qbusiness.types.message_usefulness_reason

        out["reason"] = (
            aws_sdk_qbusiness.types.message_usefulness_reason.serialize_json(
                value["reason"]
            )
        )
    if "comment" in value:
        out["comment"] = value["comment"]
    import aws_sdk_qbusiness.types.timestamp

    out["submittedAt"] = aws_sdk_qbusiness.types.timestamp.serialize_json(
        value["submitted_at"]
    )
    return out


def deserialize_json(data: dict) -> MessageUsefulnessFeedback:
    out: MessageUsefulnessFeedback = {}  # type: ignore[typeddict-item]
    if "usefulness" in data:
        import aws_sdk_qbusiness.types.message_usefulness

        out["usefulness"] = aws_sdk_qbusiness.types.message_usefulness.deserialize_json(
            data["usefulness"]
        )
    else:
        raise DeserializationError("MessageUsefulnessFeedback.usefulness required")
    if "reason" in data:
        import aws_sdk_qbusiness.types.message_usefulness_reason

        out["reason"] = (
            aws_sdk_qbusiness.types.message_usefulness_reason.deserialize_json(
                data["reason"]
            )
        )
    if "comment" in data:
        out["comment"] = data["comment"]
    if "submittedAt" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["submitted_at"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(
            data["submittedAt"]
        )
    else:
        raise DeserializationError("MessageUsefulnessFeedback.submitted_at required")
    return out
