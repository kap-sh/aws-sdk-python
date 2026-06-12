"""Generated from Smithy shape ``com.amazonaws.chime#DeletePhoneNumberRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.string


class DeletePhoneNumberRequest(TypedDict):
    phone_number_id: "aws_sdk_chime.types.string.String"
    """<p>The phone number ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeletePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeletePhoneNumberRequest:
    out: DeletePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
