"""Generated from Smithy shape ``com.amazonaws.pinpointemail#SendEmailRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pinpoint_email.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pinpoint_email.types.configuration_set_name
    import aws_sdk_pinpoint_email.types.destination
    import aws_sdk_pinpoint_email.types.email_address
    import aws_sdk_pinpoint_email.types.email_address_list
    import aws_sdk_pinpoint_email.types.email_content
    import aws_sdk_pinpoint_email.types.message_tag_list


class SendEmailRequest(TypedDict):
    from_email_address: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address.EmailAddress"
    ]
    r"""<p>The email address that you want to use as the \"From\" address for the email. The address that you specify has to be verified. </p>"""
    destination: "aws_sdk_pinpoint_email.types.destination.Destination"
    """<p>An object that contains the recipients of the email message.</p>"""
    reply_to_addresses: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address_list.EmailAddressList"
    ]
    r"""<p>The \"Reply-to\" email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.</p>"""
    feedback_forwarding_email_address: NotRequired[
        "aws_sdk_pinpoint_email.types.email_address.EmailAddress"
    ]
    """<p>The address that Amazon Pinpoint should send bounce and complaint notifications to.</p>"""
    content: "aws_sdk_pinpoint_email.types.email_content.EmailContent"
    """<p>An object that contains the body of the message. You can send either a Simple message or a Raw message.</p>"""
    email_tags: NotRequired[
        "aws_sdk_pinpoint_email.types.message_tag_list.MessageTagList"
    ]
    """<p>A list of tags, in the form of name/value pairs, to apply to an email that you send using the <code>SendEmail</code> operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events. </p>"""
    configuration_set_name: NotRequired[
        "aws_sdk_pinpoint_email.types.configuration_set_name.ConfigurationSetName"
    ]
    """<p>The name of the configuration set that you want to use when sending the email.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SendEmailRequest) -> dict:
    out: dict = {}
    if "from_email_address" in value:
        out["FromEmailAddress"] = value["from_email_address"]
    import aws_sdk_pinpoint_email.types.destination

    out["Destination"] = aws_sdk_pinpoint_email.types.destination.serialize_json(
        value["destination"]
    )
    if "reply_to_addresses" in value:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["ReplyToAddresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.serialize_json(
                value["reply_to_addresses"]
            )
        )
    if "feedback_forwarding_email_address" in value:
        out["FeedbackForwardingEmailAddress"] = value[
            "feedback_forwarding_email_address"
        ]
    import aws_sdk_pinpoint_email.types.email_content

    out["Content"] = aws_sdk_pinpoint_email.types.email_content.serialize_json(
        value["content"]
    )
    if "email_tags" in value:
        import aws_sdk_pinpoint_email.types.message_tag_list

        out["EmailTags"] = aws_sdk_pinpoint_email.types.message_tag_list.serialize_json(
            value["email_tags"]
        )
    if "configuration_set_name" in value:
        out["ConfigurationSetName"] = value["configuration_set_name"]
    return out


def deserialize_json(data: dict) -> SendEmailRequest:
    out: SendEmailRequest = {}  # type: ignore[typeddict-item]
    if "FromEmailAddress" in data:
        out["from_email_address"] = data["FromEmailAddress"]
    if "Destination" in data:
        import aws_sdk_pinpoint_email.types.destination

        out["destination"] = aws_sdk_pinpoint_email.types.destination.deserialize_json(
            data["Destination"]
        )
    else:
        raise DeserializationError("SendEmailRequest.destination required")
    if "ReplyToAddresses" in data:
        import aws_sdk_pinpoint_email.types.email_address_list

        out["reply_to_addresses"] = (
            aws_sdk_pinpoint_email.types.email_address_list.deserialize_json(
                data["ReplyToAddresses"]
            )
        )
    if "FeedbackForwardingEmailAddress" in data:
        out["feedback_forwarding_email_address"] = data[
            "FeedbackForwardingEmailAddress"
        ]
    if "Content" in data:
        import aws_sdk_pinpoint_email.types.email_content

        out["content"] = aws_sdk_pinpoint_email.types.email_content.deserialize_json(
            data["Content"]
        )
    else:
        raise DeserializationError("SendEmailRequest.content required")
    if "EmailTags" in data:
        import aws_sdk_pinpoint_email.types.message_tag_list

        out["email_tags"] = (
            aws_sdk_pinpoint_email.types.message_tag_list.deserialize_json(
                data["EmailTags"]
            )
        )
    if "ConfigurationSetName" in data:
        out["configuration_set_name"] = data["ConfigurationSetName"]
    return out
