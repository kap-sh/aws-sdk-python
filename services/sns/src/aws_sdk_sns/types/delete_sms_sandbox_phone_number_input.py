"""Generated from Smithy shape ``com.amazonaws.sns#DeleteSMSSandboxPhoneNumberInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_sns._protocol.xml import Element
from aws_sdk_sns.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_sns.types.phone_number_string


class DeleteSMSSandboxPhoneNumberInput(TypedDict):
    phone_number: "aws_sdk_sns.types.phone_number_string.PhoneNumberString"
    """<p>The destination phone number to delete.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteSMSSandboxPhoneNumberInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    pairs.append((f"{prefix}.PhoneNumber", str(value["phone_number"])))


def deserialize_query(el: Element) -> DeleteSMSSandboxPhoneNumberInput:
    out: DeleteSMSSandboxPhoneNumberInput = {}  # type: ignore[typeddict-item]
    child_phone_number = el.find("PhoneNumber")
    if child_phone_number is not None:
        out["phone_number"] = str(child_phone_number.text or "")
    else:
        raise DeserializationError(
            "DeleteSMSSandboxPhoneNumberInput.phone_number required"
        )
    return out
