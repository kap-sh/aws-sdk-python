"""Generated from Smithy shape ``com.amazonaws.chime#AssociatePhoneNumberWithUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_chime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_chime.types.e164_phone_number
    import aws_sdk_chime.types.string


class AssociatePhoneNumberWithUserRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.string.String"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "aws_sdk_chime.types.string.String"
    """<p>The user ID.</p>"""
    e164_phone_number: "aws_sdk_chime.types.e164_phone_number.E164PhoneNumber"
    """<p>The phone number, in E.164 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AssociatePhoneNumberWithUserRequest) -> dict:
    out: dict = {}
    out["E164PhoneNumber"] = value["e164_phone_number"]
    return out


def deserialize_json(data: dict) -> AssociatePhoneNumberWithUserRequest:
    out: AssociatePhoneNumberWithUserRequest = {}  # type: ignore[typeddict-item]
    if "E164PhoneNumber" in data:
        out["e164_phone_number"] = data["E164PhoneNumber"]
    else:
        raise DeserializationError(
            "AssociatePhoneNumberWithUserRequest.e164_phone_number required"
        )
    return out
