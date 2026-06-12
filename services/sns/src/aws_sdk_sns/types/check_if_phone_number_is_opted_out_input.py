"""Generated from Smithy shape ``com.amazonaws.sns#CheckIfPhoneNumberIsOptedOutInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.phone_number


class CheckIfPhoneNumberIsOptedOutInput(TypedDict):
    phone_number: "aws_sdk_sns.types.phone_number.PhoneNumber"
    """<p>The phone number for which you want to check the opt out status.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: CheckIfPhoneNumberIsOptedOutInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.phoneNumber", str(value["phone_number"])))


def deserialize_query(el: Element) -> CheckIfPhoneNumberIsOptedOutInput:
    out: CheckIfPhoneNumberIsOptedOutInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("phoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        raise DeserializationError(
            "CheckIfPhoneNumberIsOptedOutInput.phone_number required"
        )
    return out
