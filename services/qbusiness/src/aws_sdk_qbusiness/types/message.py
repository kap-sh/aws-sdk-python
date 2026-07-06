"""Generated from Smithy shape ``com.amazonaws.qbusiness#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.action_execution
    import aws_sdk_qbusiness.types.action_review
    import aws_sdk_qbusiness.types.attachments_output
    import aws_sdk_qbusiness.types.message_body
    import aws_sdk_qbusiness.types.message_type
    import aws_sdk_qbusiness.types.source_attributions
    import aws_sdk_qbusiness.types.string
    import aws_sdk_qbusiness.types.timestamp


class Message(TypedDict, closed=True):
    message_id: NotRequired["aws_sdk_qbusiness.types.string.String"]
    """<p>The identifier of the Amazon Q Business web experience message.</p>"""
    body: NotRequired["aws_sdk_qbusiness.types.message_body.MessageBody"]
    """<p>The content of the Amazon Q Business web experience message.</p>"""
    time: NotRequired["aws_sdk_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp of the first Amazon Q Business web experience message.</p>"""
    type: NotRequired["aws_sdk_qbusiness.types.message_type.MessageType"]
    """<p>The type of Amazon Q Business message, whether <code>HUMAN</code> or <code>AI</code> generated.</p>"""
    attachments: NotRequired[
        "aws_sdk_qbusiness.types.attachments_output.AttachmentsOutput"
    ]
    """<p>A file directly uploaded into an Amazon Q Business web experience chat.</p>"""
    source_attribution: NotRequired[
        "aws_sdk_qbusiness.types.source_attributions.SourceAttributions"
    ]
    """<p>The source documents used to generate Amazon Q Business web experience message.</p>"""
    action_review: NotRequired["aws_sdk_qbusiness.types.action_review.ActionReview"]
    action_execution: NotRequired[
        "aws_sdk_qbusiness.types.action_execution.ActionExecution"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "body" in value:
        out["body"] = value["body"]
    if "time" in value:
        import aws_sdk_qbusiness.types.timestamp

        out["time"] = aws_sdk_qbusiness.types.timestamp.serialize_json(value["time"])
    if "type" in value:
        import aws_sdk_qbusiness.types.message_type

        out["type"] = aws_sdk_qbusiness.types.message_type.serialize_json(value["type"])
    if "attachments" in value:
        import aws_sdk_qbusiness.types.attachments_output

        out["attachments"] = aws_sdk_qbusiness.types.attachments_output.serialize_json(
            value["attachments"]
        )
    if "source_attribution" in value:
        import aws_sdk_qbusiness.types.source_attributions

        out["sourceAttribution"] = (
            aws_sdk_qbusiness.types.source_attributions.serialize_json(
                value["source_attribution"]
            )
        )
    if "action_review" in value:
        import aws_sdk_qbusiness.types.action_review

        out["actionReview"] = aws_sdk_qbusiness.types.action_review.serialize_json(
            value["action_review"]
        )
    if "action_execution" in value:
        import aws_sdk_qbusiness.types.action_execution

        out["actionExecution"] = (
            aws_sdk_qbusiness.types.action_execution.serialize_json(
                value["action_execution"]
            )
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    if "body" in data:
        out["body"] = data["body"]
    if "time" in data:
        import aws_sdk_qbusiness.types.timestamp

        out["time"] = aws_sdk_qbusiness.types.timestamp.deserialize_json(data["time"])
    if "type" in data:
        import aws_sdk_qbusiness.types.message_type

        out["type"] = aws_sdk_qbusiness.types.message_type.deserialize_json(
            data["type"]
        )
    if "attachments" in data:
        import aws_sdk_qbusiness.types.attachments_output

        out["attachments"] = (
            aws_sdk_qbusiness.types.attachments_output.deserialize_json(
                data["attachments"]
            )
        )
    if "sourceAttribution" in data:
        import aws_sdk_qbusiness.types.source_attributions

        out["source_attribution"] = (
            aws_sdk_qbusiness.types.source_attributions.deserialize_json(
                data["sourceAttribution"]
            )
        )
    if "actionReview" in data:
        import aws_sdk_qbusiness.types.action_review

        out["action_review"] = aws_sdk_qbusiness.types.action_review.deserialize_json(
            data["actionReview"]
        )
    if "actionExecution" in data:
        import aws_sdk_qbusiness.types.action_execution

        out["action_execution"] = (
            aws_sdk_qbusiness.types.action_execution.deserialize_json(
                data["actionExecution"]
            )
        )
    return out
