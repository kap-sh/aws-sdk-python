"""Generated from Smithy shape ``com.amazonaws.sns#CreateSMSSandboxPhoneNumberInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.language_code_string
    import aws_sdk_sns.types.phone_number_string


class CreateSMSSandboxPhoneNumberInput(TypedDict):
    phone_number: "aws_sdk_sns.types.phone_number_string.PhoneNumberString"
    """<p>The destination phone number to verify. On verification, Amazon SNS adds this phone number to the list of verified phone numbers that you can send SMS messages to.</p>"""
    language_code: NotRequired[
        "aws_sdk_sns.types.language_code_string.LanguageCodeString"
    ]
    """<p>The language to use for sending the OTP. The default value is <code>en-US</code>.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CreateSMSSandboxPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PhoneNumber", str(value["phone_number"])))
    if "language_code" in value:
        import aws_sdk_sns.types.language_code_string

        aws_sdk_sns.types.language_code_string.serialize_query(
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
        import aws_sdk_sns.types.language_code_string

        out["language_code"] = aws_sdk_sns.types.language_code_string.deserialize_query(
            child_language_code
        )
    return out
