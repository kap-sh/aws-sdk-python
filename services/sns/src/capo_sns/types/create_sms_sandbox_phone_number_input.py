"""Generated from Smithy shape ``com.amazonaws.sns#CreateSMSSandboxPhoneNumberInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_sns._protocol.xml import Element
from capo_sns.errors import DeserializationError

if TYPE_CHECKING:
    import capo_sns.types.language_code_string
    import capo_sns.types.phone_number_string


class CreateSMSSandboxPhoneNumberInput(TypedDict, closed=True):
    phone_number: "capo_sns.types.phone_number_string.PhoneNumberString"
    """<p>The destination phone number to verify. On verification, Amazon SNS adds this phone number to the list of verified phone numbers that you can send SMS messages to.</p>"""
    language_code: NotRequired["capo_sns.types.language_code_string.LanguageCodeString"]
    """<p>The language to use for sending the OTP. The default value is <code>en-US</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSMSSandboxPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PhoneNumber", str(value["phone_number"])))
    if "language_code" in value:
        import capo_sns.types.language_code_string

        capo_sns.types.language_code_string.serialize_query(
            value["language_code"], pairs, f"{prefix}.LanguageCode"
        )


def deserialize_query(el: Element) -> CreateSMSSandboxPhoneNumberInput:
    out: CreateSMSSandboxPhoneNumberInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        raise DeserializationError(
            "CreateSMSSandboxPhoneNumberInput.phone_number required"
        )
    child_language_code = el.find("LanguageCode")
    if child_language_code is not None:
        import capo_sns.types.language_code_string

        out["language_code"] = capo_sns.types.language_code_string.deserialize_query(
            child_language_code
        )
    return out
