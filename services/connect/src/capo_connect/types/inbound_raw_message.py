"""Generated from Smithy shape ``com.amazonaws.connect#InboundRawMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.body
    import capo_connect.types.email_headers
    import capo_connect.types.email_message_content_type
    import capo_connect.types.inbound_subject


class InboundRawMessage(TypedDict, closed=True):
    subject: "capo_connect.types.inbound_subject.InboundSubject"
    """<p>The email subject.</p>"""
    body: "capo_connect.types.body.Body"
    """<p>The email message body.</p>"""
    content_type: (
        "capo_connect.types.email_message_content_type.EmailMessageContentType"
    )
    """<p>Type of content, that is, <code>text/plain</code> or <code>text/html</code>.</p>"""
    headers: NotRequired["capo_connect.types.email_headers.EmailHeaders"]
    """<p>Headers present in inbound email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InboundRawMessage) -> dict:
    out: dict = {}
    out["Subject"] = value["subject"]
    out["Body"] = value["body"]
    out["ContentType"] = value["content_type"]
    if "headers" in value:
        import capo_connect.types.email_headers

        out["Headers"] = capo_connect.types.email_headers.serialize_json(
            value["headers"]
        )
    return out


def deserialize_json(data: dict) -> InboundRawMessage:
    out: InboundRawMessage = {}  # type: ignore[typeddict-item]
    if "Subject" in data:
        out["subject"] = data["Subject"]
    else:
        raise DeserializationError("InboundRawMessage.subject required")
    if "Body" in data:
        out["body"] = data["Body"]
    else:
        raise DeserializationError("InboundRawMessage.body required")
    if "ContentType" in data:
        out["content_type"] = data["ContentType"]
    else:
        raise DeserializationError("InboundRawMessage.content_type required")
    if "Headers" in data:
        import capo_connect.types.email_headers

        out["headers"] = capo_connect.types.email_headers.deserialize_json(
            data["Headers"]
        )
    return out
