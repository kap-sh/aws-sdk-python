"""Generated from Smithy shape ``com.amazonaws.socialmessaging#AssociateWhatsAppBusinessAccountInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.whats_app_setup_finalization
    import aws_sdk_socialmessaging.types.whats_app_signup_callback


class AssociateWhatsAppBusinessAccountInput(TypedDict):
    signup_callback: NotRequired[
        "aws_sdk_socialmessaging.types.whats_app_signup_callback.WhatsAppSignupCallback"
    ]
    """<p>Contains the callback access token.</p>"""
    setup_finalization: NotRequired[
        "aws_sdk_socialmessaging.types.whats_app_setup_finalization.WhatsAppSetupFinalization"
    ]
    """<p>A JSON object that contains the phone numbers and WhatsApp Business Account to link to your account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociateWhatsAppBusinessAccountInput) -> dict:
    out: dict = {}
    if "signup_callback" in value:
        import aws_sdk_socialmessaging.types.whats_app_signup_callback

        out["signupCallback"] = (
            aws_sdk_socialmessaging.types.whats_app_signup_callback.serialize_json(
                value["signup_callback"]
            )
        )
    if "setup_finalization" in value:
        import aws_sdk_socialmessaging.types.whats_app_setup_finalization

        out["setupFinalization"] = (
            aws_sdk_socialmessaging.types.whats_app_setup_finalization.serialize_json(
                value["setup_finalization"]
            )
        )
    return out


def deserialize_json(data: dict) -> AssociateWhatsAppBusinessAccountInput:
    out: AssociateWhatsAppBusinessAccountInput = {}  # type: ignore[typeddict-item]
    if "signupCallback" in data:
        import aws_sdk_socialmessaging.types.whats_app_signup_callback

        out["signup_callback"] = (
            aws_sdk_socialmessaging.types.whats_app_signup_callback.deserialize_json(
                data["signupCallback"]
            )
        )
    if "setupFinalization" in data:
        import aws_sdk_socialmessaging.types.whats_app_setup_finalization

        out["setup_finalization"] = (
            aws_sdk_socialmessaging.types.whats_app_setup_finalization.deserialize_json(
                data["setupFinalization"]
            )
        )
    return out
