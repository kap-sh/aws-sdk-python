"""Generated from Smithy shape ``com.amazonaws.connect#ClaimPhoneNumberResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.arn
    import capo_connect.types.phone_number_id


class ClaimPhoneNumberResponse(TypedDict, closed=True):
    phone_number_id: NotRequired["capo_connect.types.phone_number_id.PhoneNumberId"]
    """<p>A unique identifier for the phone number.</p>"""
    phone_number_arn: NotRequired["capo_connect.types.arn.ARN"]
    """<p>The Amazon Resource Name (ARN) of the phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClaimPhoneNumberResponse) -> dict:
    out: dict = {}
    if "phone_number_id" in value:
        out["PhoneNumberId"] = value["phone_number_id"]
    if "phone_number_arn" in value:
        out["PhoneNumberArn"] = value["phone_number_arn"]
    return out


def deserialize_json(data: dict) -> ClaimPhoneNumberResponse:
    out: ClaimPhoneNumberResponse = {}  # type: ignore[typeddict-item]
    if "PhoneNumberId" in data:
        out["phone_number_id"] = data["PhoneNumberId"]
    if "PhoneNumberArn" in data:
        out["phone_number_arn"] = data["PhoneNumberArn"]
    return out
