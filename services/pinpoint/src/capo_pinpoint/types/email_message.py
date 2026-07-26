"""Generated from Smithy shape ``com.amazonaws.pinpoint#EmailMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint.types.__string
    import capo_pinpoint.types.list_of__string
    import capo_pinpoint.types.map_of_list_of__string
    import capo_pinpoint.types.raw_email
    import capo_pinpoint.types.simple_email


class EmailMessage(TypedDict, closed=True):
    body: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The body of the email message.</p>"""
    feedback_forwarding_address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The email address to forward bounces and complaints to, if feedback forwarding is enabled.</p>"""
    from_address: NotRequired["capo_pinpoint.types.__string.__string"]
    """<p>The verified email address to send the email message from. The default value is the FromAddress specified for the email channel.</p>"""
    raw_email: NotRequired["capo_pinpoint.types.raw_email.RawEmail"]
    """<p>The email message, represented as a raw MIME message.</p>"""
    reply_to_addresses: NotRequired[
        "capo_pinpoint.types.list_of__string.ListOf__string"
    ]
    """<p>The reply-to email address(es) for the email message. If a recipient replies to the email, each reply-to address receives the reply.</p>"""
    simple_email: NotRequired["capo_pinpoint.types.simple_email.SimpleEmail"]
    """<p>The email message, composed of a subject, a text part, and an HTML part.</p>"""
    substitutions: NotRequired[
        "capo_pinpoint.types.map_of_list_of__string.MapOfListOf__string"
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
        import capo_pinpoint.types.raw_email

        out["RawEmail"] = capo_pinpoint.types.raw_email.serialize_json(
            value["raw_email"]
        )
    if "reply_to_addresses" in value:
        import capo_pinpoint.types.list_of__string

        out["ReplyToAddresses"] = capo_pinpoint.types.list_of__string.serialize_json(
            value["reply_to_addresses"]
        )
    if "simple_email" in value:
        import capo_pinpoint.types.simple_email

        out["SimpleEmail"] = capo_pinpoint.types.simple_email.serialize_json(
            value["simple_email"]
        )
    if "substitutions" in value:
        import capo_pinpoint.types.map_of_list_of__string

        out["Substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.serialize_json(
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
        import capo_pinpoint.types.raw_email

        out["raw_email"] = capo_pinpoint.types.raw_email.deserialize_json(
            data["RawEmail"]
        )
    if "ReplyToAddresses" in data:
        import capo_pinpoint.types.list_of__string

        out["reply_to_addresses"] = (
            capo_pinpoint.types.list_of__string.deserialize_json(
                data["ReplyToAddresses"]
            )
        )
    if "SimpleEmail" in data:
        import capo_pinpoint.types.simple_email

        out["simple_email"] = capo_pinpoint.types.simple_email.deserialize_json(
            data["SimpleEmail"]
        )
    if "Substitutions" in data:
        import capo_pinpoint.types.map_of_list_of__string

        out["substitutions"] = (
            capo_pinpoint.types.map_of_list_of__string.deserialize_json(
                data["Substitutions"]
            )
        )
    return out
