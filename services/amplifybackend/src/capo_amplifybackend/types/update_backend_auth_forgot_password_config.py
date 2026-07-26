"""Generated from Smithy shape ``com.amazonaws.amplifybackend#UpdateBackendAuthForgotPasswordConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.delivery_method
    import capo_amplifybackend.types.email_settings
    import capo_amplifybackend.types.sms_settings


class UpdateBackendAuthForgotPasswordConfig(TypedDict, closed=True):
    delivery_method: NotRequired[
        "capo_amplifybackend.types.delivery_method.DeliveryMethod"
    ]
    """<p><b>(DEPRECATED)</b> Describes which mode to use (either SMS or email) to deliver messages to app users that want to recover their password.</p>"""
    email_settings: NotRequired[
        "capo_amplifybackend.types.email_settings.EmailSettings"
    ]
    """<p><b>(DEPRECATED)</b> The configuration for the email sent when an app user forgets their password.</p>"""
    sms_settings: NotRequired["capo_amplifybackend.types.sms_settings.SmsSettings"]
    """<p><b>(DEPRECATED)</b> The configuration for the SMS message sent when an Amplify app user forgets their password.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBackendAuthForgotPasswordConfig) -> dict:
    out: dict = {}
    if "delivery_method" in value:
        import capo_amplifybackend.types.delivery_method

        out["deliveryMethod"] = (
            capo_amplifybackend.types.delivery_method.serialize_json(
                value["delivery_method"]
            )
        )
    if "email_settings" in value:
        import capo_amplifybackend.types.email_settings

        out["emailSettings"] = capo_amplifybackend.types.email_settings.serialize_json(
            value["email_settings"]
        )
    if "sms_settings" in value:
        import capo_amplifybackend.types.sms_settings

        out["smsSettings"] = capo_amplifybackend.types.sms_settings.serialize_json(
            value["sms_settings"]
        )
    return out


def deserialize_json(data: dict) -> UpdateBackendAuthForgotPasswordConfig:
    out: UpdateBackendAuthForgotPasswordConfig = {}  # type: ignore[typeddict-item]
    if "deliveryMethod" in data:
        import capo_amplifybackend.types.delivery_method

        out["delivery_method"] = (
            capo_amplifybackend.types.delivery_method.deserialize_json(
                data["deliveryMethod"]
            )
        )
    if "emailSettings" in data:
        import capo_amplifybackend.types.email_settings

        out["email_settings"] = (
            capo_amplifybackend.types.email_settings.deserialize_json(
                data["emailSettings"]
            )
        )
    if "smsSettings" in data:
        import capo_amplifybackend.types.sms_settings

        out["sms_settings"] = capo_amplifybackend.types.sms_settings.deserialize_json(
            data["smsSettings"]
        )
    return out
