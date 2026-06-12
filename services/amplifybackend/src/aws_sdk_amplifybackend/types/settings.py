"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Settings``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_amplifybackend.types.__string
    import aws_sdk_amplifybackend.types.list_of_mfa_types_element


class Settings(TypedDict):
    mfa_types: NotRequired[
        "aws_sdk_amplifybackend.types.list_of_mfa_types_element.ListOfMfaTypesElement"
    ]
    """<p>The supported MFA types.</p>"""
    sms_message: NotRequired["aws_sdk_amplifybackend.types.__string.__string"]
    """<p>The body of the SMS message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Settings) -> dict:
    out: dict = {}
    if "mfa_types" in value:
        import aws_sdk_amplifybackend.types.list_of_mfa_types_element

        out["mfaTypes"] = (
            aws_sdk_amplifybackend.types.list_of_mfa_types_element.serialize_json(
                value["mfa_types"]
            )
        )
    if "sms_message" in value:
        out["smsMessage"] = value["sms_message"]
    return out


def deserialize_json(data: dict) -> Settings:
    out: Settings = {}  # type: ignore[typeddict-item]
    if "mfaTypes" in data:
        import aws_sdk_amplifybackend.types.list_of_mfa_types_element

        out["mfa_types"] = (
            aws_sdk_amplifybackend.types.list_of_mfa_types_element.deserialize_json(
                data["mfaTypes"]
            )
        )
    if "smsMessage" in data:
        out["sms_message"] = data["smsMessage"]
    return out
