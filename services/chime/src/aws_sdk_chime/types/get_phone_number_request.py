"""Generated from Smithy shape ``com.amazonaws.chime#GetPhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.string


class GetPhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: "aws_sdk_chime.types.string.String"
    """<p>The phone number ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPhoneNumberRequest:
    out: GetPhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
