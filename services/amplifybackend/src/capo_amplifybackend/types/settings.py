"""Generated from Smithy shape ``com.amazonaws.amplifybackend#Settings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_amplifybackend.types.__string
    import capo_amplifybackend.types.list_of_mfa_types_element


class Settings(TypedDict, closed=True):
    mfa_types: NotRequired[
        "capo_amplifybackend.types.list_of_mfa_types_element.ListOfMfaTypesElement"
    ]
    """<p>The supported MFA types.</p>"""
    sms_message: NotRequired["capo_amplifybackend.types.__string.__string"]
    """<p>The body of the SMS message.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Settings) -> dict:
    out: dict = {}
    if "mfa_types" in value:
        import capo_amplifybackend.types.list_of_mfa_types_element

        out["mfaTypes"] = (
            capo_amplifybackend.types.list_of_mfa_types_element.serialize_json(
                value["mfa_types"]
            )
        )
    if "sms_message" in value:
        out["smsMessage"] = value["sms_message"]
    return out


def deserialize_json(data: dict) -> Settings:
    out: Settings = {}  # type: ignore[typeddict-item]
    if "mfaTypes" in data:
        import capo_amplifybackend.types.list_of_mfa_types_element

        out["mfa_types"] = (
            capo_amplifybackend.types.list_of_mfa_types_element.deserialize_json(
                data["mfaTypes"]
            )
        )
    if "smsMessage" in data:
        out["sms_message"] = data["smsMessage"]
    return out
