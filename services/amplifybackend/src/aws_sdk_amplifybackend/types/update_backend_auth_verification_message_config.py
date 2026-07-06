"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthVerificationMessageConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.delivery_method
    import aws_sdk_amplifybackend.types.email_settings
    import aws_sdk_amplifybackend.types.sms_settings


class UpdateBackendAuthVerificationMessageConfig(TypedDict, closed=True):
    delivery_method: NotRequired[
        "aws_sdk_amplifybackend.types.delivery_method.DeliveryMethod"
    ]
    """<p>The type of verification message to send.</p>"""
    email_settings: NotRequired[
        "aws_sdk_amplifybackend.types.email_settings.EmailSettings"
    ]
    """<p>The settings for the email message.</p>"""
    sms_settings: NotRequired["aws_sdk_amplifybackend.types.sms_settings.SmsSettings"]
    """<p>The settings for the SMS message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthVerificationMessageConfig) -> dict:
    out: dict = {}
    if "delivery_method" in value:
        import aws_sdk_amplifybackend.types.delivery_method

        out["deliveryMethod"] = (
            aws_sdk_amplifybackend.types.delivery_method.serialize_json(
                value["delivery_method"]
            )
        )
    if "email_settings" in value:
        import aws_sdk_amplifybackend.types.email_settings

        out["emailSettings"] = (
            aws_sdk_amplifybackend.types.email_settings.serialize_json(
                value["email_settings"]
            )
        )
    if "sms_settings" in value:
        import aws_sdk_amplifybackend.types.sms_settings

        out["smsSettings"] = aws_sdk_amplifybackend.types.sms_settings.serialize_json(
            value["sms_settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthVerificationMessageConfig:
    out: UpdateBackendAuthVerificationMessageConfig = {}  # type: ignore[typeddict-item]
    if "deliveryMethod" in data:
        import aws_sdk_amplifybackend.types.delivery_method

        out["delivery_method"] = (
            aws_sdk_amplifybackend.types.delivery_method.deserialize_json(
                data["deliveryMethod"]
            )
        )
    if "emailSettings" in data:
        import aws_sdk_amplifybackend.types.email_settings

        out["email_settings"] = (
            aws_sdk_amplifybackend.types.email_settings.deserialize_json(
                data["emailSettings"]
            )
        )
    if "smsSettings" in data:
        import aws_sdk_amplifybackend.types.sms_settings

        out["sms_settings"] = (
            aws_sdk_amplifybackend.types.sms_settings.deserialize_json(
                data["smsSettings"]
            )
        )
    return out
