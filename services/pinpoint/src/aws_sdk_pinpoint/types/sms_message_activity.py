"""Generated from Smithy shape ``com.amazonaws.pinpoint#SMSMessageActivity``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.__string
    import aws_sdk_pinpoint.types.journey_sms_message


class SMSMessageActivity(TypedDict):
    message_config: NotRequired[
        "aws_sdk_pinpoint.types.journey_sms_message.JourneySMSMessage"
    ]
    """<p>Specifies the sender ID and message type for an SMS message that's sent to participants in a journey.</p>"""
    next_activity: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the next activity to perform, after the message is sent.</p>"""
    template_name: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The name of the SMS message template to use for the message. If specified, this value must match the name of an existing message template.</p>"""
    template_version: NotRequired["aws_sdk_pinpoint.types.__string.__string"]
    """<p>The unique identifier for the version of the SMS template to use for the message. If specified, this value must match the identifier for an existing template version. To retrieve a list of versions and version identifiers for a template, use the <link linkend=\"templates-template-name-template-type-versions\">Template Versions</link> resource.</p> <p>If you don't specify a value for this property, Amazon Pinpoint uses the <i>active version</i> of the template. The <i>active version</i> is typically the version of a template that's been most recently reviewed and approved for use, depending on your workflow. It isn't necessarily the latest version of a template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SMSMessageActivity) -> dict:
    out: dict = {}
    if "message_config" in value:
        import aws_sdk_pinpoint.types.journey_sms_message

        out["MessageConfig"] = (
            aws_sdk_pinpoint.types.journey_sms_message.serialize_json(
                value["message_config"]
            )
        )
    if "next_activity" in value:
        out["NextActivity"] = value["next_activity"]
    if "template_name" in value:
        out["TemplateName"] = value["template_name"]
    if "template_version" in value:
        out["TemplateVersion"] = value["template_version"]
    return out


def deserialize_json(data: dict) -> SMSMessageActivity:
    out: SMSMessageActivity = {}  # type: ignore[typeddict-item]
    if "MessageConfig" in data:
        import aws_sdk_pinpoint.types.journey_sms_message

        out["message_config"] = (
            aws_sdk_pinpoint.types.journey_sms_message.deserialize_json(
                data["MessageConfig"]
            )
        )
    if "NextActivity" in data:
        out["next_activity"] = data["NextActivity"]
    if "TemplateName" in data:
        out["template_name"] = data["TemplateName"]
    if "TemplateVersion" in data:
        out["template_version"] = data["TemplateVersion"]
    return out
