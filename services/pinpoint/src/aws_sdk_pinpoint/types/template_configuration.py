"""Generated from Smithy shape ``com.amazonaws.pinpoint#TemplateConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_pinpoint.types.template


class TemplateConfiguration(TypedDict, closed=True):
    email_template: NotRequired["aws_sdk_pinpoint.types.template.Template"]
    """<p>The email template to use for the message.</p>"""
    push_template: NotRequired["aws_sdk_pinpoint.types.template.Template"]
    """<p>The push notification template to use for the message.</p>"""
    sms_template: NotRequired["aws_sdk_pinpoint.types.template.Template"]
    """<p>The SMS template to use for the message.</p>"""
    voice_template: NotRequired["aws_sdk_pinpoint.types.template.Template"]
    """<p>The voice template to use for the message. This object isn't supported for campaigns.</p>"""
    in_app_template: NotRequired["aws_sdk_pinpoint.types.template.Template"]
    """<p>The InApp template to use for the message. The InApp template object is not supported for SendMessages.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TemplateConfiguration) -> dict:
    out: dict = {}
    if "email_template" in value:
        import aws_sdk_pinpoint.types.template

        out["EmailTemplate"] = aws_sdk_pinpoint.types.template.serialize_json(
            value["email_template"]
        )
    if "push_template" in value:
        import aws_sdk_pinpoint.types.template

        out["PushTemplate"] = aws_sdk_pinpoint.types.template.serialize_json(
            value["push_template"]
        )
    if "sms_template" in value:
        import aws_sdk_pinpoint.types.template

        out["SMSTemplate"] = aws_sdk_pinpoint.types.template.serialize_json(
            value["sms_template"]
        )
    if "voice_template" in value:
        import aws_sdk_pinpoint.types.template

        out["VoiceTemplate"] = aws_sdk_pinpoint.types.template.serialize_json(
            value["voice_template"]
        )
    if "in_app_template" in value:
        import aws_sdk_pinpoint.types.template

        out["InAppTemplate"] = aws_sdk_pinpoint.types.template.serialize_json(
            value["in_app_template"]
        )
    return out


def deserialize_json(data: dict) -> TemplateConfiguration:
    out: TemplateConfiguration = {}  # type: ignore[typeddict-item]
    if "EmailTemplate" in data:
        import aws_sdk_pinpoint.types.template

        out["email_template"] = aws_sdk_pinpoint.types.template.deserialize_json(
            data["EmailTemplate"]
        )
    if "PushTemplate" in data:
        import aws_sdk_pinpoint.types.template

        out["push_template"] = aws_sdk_pinpoint.types.template.deserialize_json(
            data["PushTemplate"]
        )
    if "SMSTemplate" in data:
        import aws_sdk_pinpoint.types.template

        out["sms_template"] = aws_sdk_pinpoint.types.template.deserialize_json(
            data["SMSTemplate"]
        )
    if "VoiceTemplate" in data:
        import aws_sdk_pinpoint.types.template

        out["voice_template"] = aws_sdk_pinpoint.types.template.deserialize_json(
            data["VoiceTemplate"]
        )
    if "InAppTemplate" in data:
        import aws_sdk_pinpoint.types.template

        out["in_app_template"] = aws_sdk_pinpoint.types.template.deserialize_json(
            data["InAppTemplate"]
        )
    return out
