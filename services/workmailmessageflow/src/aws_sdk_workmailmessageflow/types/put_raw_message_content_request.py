"""Generated from Smithy shape ``com.amazonaws.workmailmessageflow#PutRawMessageContentRequest``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_workmailmessageflow.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_workmailmessageflow.types.message_id_type
    import aws_sdk_workmailmessageflow.types.raw_message_content


class PutRawMessageContentRequest(TypedDict):
    message_id: "aws_sdk_workmailmessageflow.types.message_id_type.messageIdType"
    """<p>The identifier of the email message being updated.</p>"""
    content: "aws_sdk_workmailmessageflow.types.raw_message_content.RawMessageContent"
    """<p>Describes the raw message content of the updated email message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRawMessageContentRequest) -> dict:
    out: dict = {}
    import aws_sdk_workmailmessageflow.types.raw_message_content

    out["content"] = (
        aws_sdk_workmailmessageflow.types.raw_message_content.serialize_json(
            value["content"]
        )
    )
    return out


def deserialize_json(data: dict) -> PutRawMessageContentRequest:
    out: PutRawMessageContentRequest = {}  # type: ignore[typeddict-item]
    if "content" in data:
        import aws_sdk_workmailmessageflow.types.raw_message_content

        out["content"] = (
            aws_sdk_workmailmessageflow.types.raw_message_content.deserialize_json(
                data["content"]
            )
        )
    else:
        raise DeserializationError("PutRawMessageContentRequest.content required")
    return out
