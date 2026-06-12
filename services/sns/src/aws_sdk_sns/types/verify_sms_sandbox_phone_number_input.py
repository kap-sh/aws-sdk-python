"""Generated from Smithy shape ``com.amazonaws.sns#VerifySMSSandboxPhoneNumberInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.otp_code
    import aws_sdk_sns.types.phone_number_string


class VerifySMSSandboxPhoneNumberInput(TypedDict):
    phone_number: "aws_sdk_sns.types.phone_number_string.PhoneNumberString"
    """<p>The destination phone number to verify.</p>"""
    one_time_password: "aws_sdk_sns.types.otp_code.OTPCode"
    """<p>The OTP sent to the destination number from the <code>CreateSMSSandBoxPhoneNumber</code> call.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: VerifySMSSandboxPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PhoneNumber", str(value["phone_number"])))
    pairs.append((f"{prefix}.OneTimePassword", str(value["one_time_password"])))


def deserialize_query(el: Element) -> VerifySMSSandboxPhoneNumberInput:
    out: VerifySMSSandboxPhoneNumberInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        raise DeserializationError(
            "VerifySMSSandboxPhoneNumberInput.phone_number required"
        )
    child_one_time_password = el.find("OneTimePassword")
    if child_one_time_password is not None:
        out["one_time_password"] = str(child_one_time_password.text or "")
    else:
        raise DeserializationError(
            "VerifySMSSandboxPhoneNumberInput.one_time_password required"
        )
    return out
