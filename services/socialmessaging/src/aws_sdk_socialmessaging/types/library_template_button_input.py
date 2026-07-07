"""Generated from Smithy shape ``com.amazonaws.socialmessaging#LibraryTemplateButtonInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_socialmessaging.types.button_type
    import aws_sdk_socialmessaging.types.meta_url_with_suffix_example
    import aws_sdk_socialmessaging.types.otp_type
    import aws_sdk_socialmessaging.types.phone_number
    import aws_sdk_socialmessaging.types.supported_apps
    import aws_sdk_socialmessaging.types.zero_tap_terms_accepted


class LibraryTemplateButtonInput(TypedDict, closed=True):
    type: NotRequired["aws_sdk_socialmessaging.types.button_type.ButtonType"]
    """<p>The type of button (for example, QUICK_REPLY, CALL, or URL).</p>"""
    phone_number: NotRequired["aws_sdk_socialmessaging.types.phone_number.PhoneNumber"]
    """<p>The phone number in E.164 format for CALL-type buttons.</p>"""
    url: NotRequired[
        "aws_sdk_socialmessaging.types.meta_url_with_suffix_example.MetaUrlWithSuffixExample"
    ]
    """<p>The URL with dynamic parameters for URL-type buttons.</p>"""
    otp_type: NotRequired["aws_sdk_socialmessaging.types.otp_type.OtpType"]
    """<p>The type of one-time password for OTP buttons.</p>"""
    zero_tap_terms_accepted: NotRequired[
        "aws_sdk_socialmessaging.types.zero_tap_terms_accepted.ZeroTapTermsAccepted"
    ]
    """<p>When true, indicates acceptance of zero-tap terms for the button.</p>"""
    supported_apps: NotRequired[
        "aws_sdk_socialmessaging.types.supported_apps.SupportedApps"
    ]
    """<p>List of supported applications for this button type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LibraryTemplateButtonInput) -> dict:
    out: dict = {}
    if "type" in value:
        out["type"] = value["type"]
    if "phone_number" in value:
        out["phoneNumber"] = value["phone_number"]
    if "url" in value:
        import aws_sdk_socialmessaging.types.meta_url_with_suffix_example

        out["url"] = (
            aws_sdk_socialmessaging.types.meta_url_with_suffix_example.serialize_json(
                value["url"]
            )
        )
    if "otp_type" in value:
        out["otpType"] = value["otp_type"]
    if "zero_tap_terms_accepted" in value:
        out["zeroTapTermsAccepted"] = value["zero_tap_terms_accepted"]
    if "supported_apps" in value:
        import aws_sdk_socialmessaging.types.supported_apps

        out["supportedApps"] = (
            aws_sdk_socialmessaging.types.supported_apps.serialize_json(
                value["supported_apps"]
            )
        )
    return out


def deserialize_json(data: dict) -> LibraryTemplateButtonInput:
    out: LibraryTemplateButtonInput = {}  # type: ignore[typeddict-item]
    if "type" in data:
        out["type"] = data["type"]
    if "phoneNumber" in data:
        out["phone_number"] = data["phoneNumber"]
    if "url" in data:
        import aws_sdk_socialmessaging.types.meta_url_with_suffix_example

        out["url"] = (
            aws_sdk_socialmessaging.types.meta_url_with_suffix_example.deserialize_json(
                data["url"]
            )
        )
    if "otpType" in data:
        out["otp_type"] = data["otpType"]
    if "zeroTapTermsAccepted" in data:
        out["zero_tap_terms_accepted"] = data["zeroTapTermsAccepted"]
    if "supportedApps" in data:
        import aws_sdk_socialmessaging.types.supported_apps

        out["supported_apps"] = (
            aws_sdk_socialmessaging.types.supported_apps.deserialize_json(
                data["supportedApps"]
            )
        )
    return out
