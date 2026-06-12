"""Generated from Smithy shape ``com.amazonaws.connect#DescribePhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_connect.types.phone_number_id


class DescribePhoneNumberRequest(TypedDict):
    phone_number_id: "aws_sdk_connect.types.phone_number_id.PhoneNumberId"
    """<p>A unique identifier for the phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribePhoneNumberRequest:
    out: DescribePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
