"""Generated from Smithy shape ``com.amazonaws.pinpoint#EmailMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.list_of__string
    import aws_sdk_pinpoint.types.map_of_list_of__string
    import aws_sdk_pinpoint.types.raw_email
    import aws_sdk_pinpoint.types.simple_email


class EmailMessage(TypedDict, closed=True):
    body: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The body of the email message.</p>"""
    feedback_forwarding_address: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The email address to forward bounces and complaints to, if feedback forwarding is enabled.</p>"""
    from_address: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The verified email address to send the email message from. The default value is the FromAddress specified for the email channel.</p>"""
    raw_email: NotRequired["aws_sdk_pinpoint.types.raw_email.RawEmail"]
    """<p>The email message, represented as a raw MIME message.</p>"""
    reply_to_addresses: NotRequired[
        "aws_sdk_pinpoint.types.list_of__string.ListOf__string"
    ]
    """<p>The reply-to email address(es) for the email message. If a recipient replies to the email, each reply-to address receives the reply.</p>"""
    simple_email: NotRequired["aws_sdk_pinpoint.types.simple_email.SimpleEmail"]
    """<p>The email message, composed of a subject, a text part, and an HTML part.</p>"""
    substitutions: NotRequired[
        "aws_sdk_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
    ]
    """<p>The default message variables to use in the email message. You can override the default variables with individual address variables.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EmailMessage) -> dict:
    out: dict = {}
    if "body" in value:
        out["Body"] = value["body"]
    if "feedback_forwarding_address" in value:
        out["FeedbackForwardingAddress"] = value["feedback_forwarding_address"]
    if "from_address" in value:
        out["FromAddress"] = value["from_address"]
    if "raw_email" in value:
        import aws_sdk_pinpoint.types.raw_email

        out["RawEmail"] = aws_sdk_pinpoint.types.raw_email.serialize_json(
            value["raw_email"]
        )
    if "reply_to_addresses" in value:
        import aws_sdk_pinpoint.types.list_of__string

        out["ReplyToAddresses"] = aws_sdk_pinpoint.types.list_of__string.serialize_json(
            value["reply_to_addresses"]
        )
    if "simple_email" in value:
        import aws_sdk_pinpoint.types.simple_email

        out["SimpleEmail"] = aws_sdk_pinpoint.types.simple_email.serialize_json(
            value["simple_email"]
        )
    if "substitutions" in value:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.serialize_json(
                value["substitutions"]
            )
        )
    return out


def deserialize_json(data: dict) -> EmailMessage:
    out: EmailMessage = {}  # type: ignore[typeddict-item]
    if "Body" in data:
        out["body"] = data["Body"]
    if "FeedbackForwardingAddress" in data:
        out["feedback_forwarding_address"] = data["FeedbackForwardingAddress"]
    if "FromAddress" in data:
        out["from_address"] = data["FromAddress"]
    if "RawEmail" in data:
        import aws_sdk_pinpoint.types.raw_email

        out["raw_email"] = aws_sdk_pinpoint.types.raw_email.deserialize_json(
            data["RawEmail"]
        )
    if "ReplyToAddresses" in data:
        import aws_sdk_pinpoint.types.list_of__string

        out["reply_to_addresses"] = (
            aws_sdk_pinpoint.types.list_of__string.deserialize_json(
                data["ReplyToAddresses"]
            )
        )
    if "SimpleEmail" in data:
        import aws_sdk_pinpoint.types.simple_email

        out["simple_email"] = aws_sdk_pinpoint.types.simple_email.deserialize_json(
            data["SimpleEmail"]
        )
    if "Substitutions" in data:
        import aws_sdk_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            aws_sdk_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    return out
