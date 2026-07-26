"""Generated from Smithy shape ``com.amazonaws.qbusiness#Message``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qbusiness.types.action_execution
    import capo_qbusiness.types.action_review
    import capo_qbusiness.types.attachments_output
    import capo_qbusiness.types.message_body
    import capo_qbusiness.types.message_type
    import capo_qbusiness.types.source_attributions
    import capo_qbusiness.types.string
    import capo_qbusiness.types.timestamp


class Message(TypedDict, closed=True):
    message_id: NotRequired["capo_qbusiness.types.string.String"]
    """<p>The identifier of the Amazon Q Business web experience message.</p>"""
    body: NotRequired["capo_qbusiness.types.message_body.MessageBody"]
    """<p>The content of the Amazon Q Business web experience message.</p>"""
    time: NotRequired["capo_qbusiness.types.timestamp.Timestamp"]
    """<p>The timestamp of the first Amazon Q Business web experience message.</p>"""
    type: NotRequired["capo_qbusiness.types.message_type.MessageType"]
    """<p>The type of Amazon Q Business message, whether <code>HUMAN</code> or <code>AI</code> generated.</p>"""
    attachments: NotRequired[
        "capo_qbusiness.types.attachments_output.AttachmentsOutput"
    ]
    """<p>A file directly uploaded into an Amazon Q Business web experience chat.</p>"""
    source_attribution: NotRequired[
        "capo_qbusiness.types.source_attributions.SourceAttributions"
    ]
    """<p>The source documents used to generate Amazon Q Business web experience message.</p>"""
    action_review: NotRequired["capo_qbusiness.types.action_review.ActionReview"]
    action_execution: NotRequired[
        "capo_qbusiness.types.action_execution.ActionExecution"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: Message) -> dict:
    out: dict = {}
    if "message_id" in value:
        out["messageId"] = value["message_id"]
    if "body" in value:
        out["body"] = value["body"]
    if "time" in value:
        import capo_qbusiness.types.timestamp

        out["time"] = capo_qbusiness.types.timestamp.serialize_json(value["time"])
    if "type" in value:
        import capo_qbusiness.types.message_type

        out["type"] = capo_qbusiness.types.message_type.serialize_json(value["type"])
    if "attachments" in value:
        import capo_qbusiness.types.attachments_output

        out["attachments"] = capo_qbusiness.types.attachments_output.serialize_json(
            value["attachments"]
        )
    if "source_attribution" in value:
        import capo_qbusiness.types.source_attributions

        out["sourceAttribution"] = (
            capo_qbusiness.types.source_attributions.serialize_json(
                value["source_attribution"]
            )
        )
    if "action_review" in value:
        import capo_qbusiness.types.action_review

        out["actionReview"] = capo_qbusiness.types.action_review.serialize_json(
            value["action_review"]
        )
    if "action_execution" in value:
        import capo_qbusiness.types.action_execution

        out["actionExecution"] = capo_qbusiness.types.action_execution.serialize_json(
            value["action_execution"]
        )
    return out


def deserialize_json(data: dict) -> Message:
    out: Message = {}  # type: ignore[typeddict-item]
    if "messageId" in data:
        out["message_id"] = data["messageId"]
    if "body" in data:
        out["body"] = data["body"]
    if "time" in data:
        import capo_qbusiness.types.timestamp

        out["time"] = capo_qbusiness.types.timestamp.deserialize_json(data["time"])
    if "type" in data:
        import capo_qbusiness.types.message_type

        out["type"] = capo_qbusiness.types.message_type.deserialize_json(data["type"])
    if "attachments" in data:
        import capo_qbusiness.types.attachments_output

        out["attachments"] = capo_qbusiness.types.attachments_output.deserialize_json(
            data["attachments"]
        )
    if "sourceAttribution" in data:
        import capo_qbusiness.types.source_attributions

        out["source_attribution"] = (
            capo_qbusiness.types.source_attributions.deserialize_json(
                data["sourceAttribution"]
            )
        )
    if "actionReview" in data:
        import capo_qbusiness.types.action_review

        out["action_review"] = capo_qbusiness.types.action_review.deserialize_json(
            data["actionReview"]
        )
    if "actionExecution" in data:
        import capo_qbusiness.types.action_execution

        out["action_execution"] = (
            capo_qbusiness.types.action_execution.deserialize_json(
                data["actionExecution"]
            )
        )
    return out
