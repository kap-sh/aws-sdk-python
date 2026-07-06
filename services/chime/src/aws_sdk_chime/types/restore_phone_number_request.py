"""Generated from Smithy shape ``com.amazonaws.chime#RestorePhoneNumberRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.non_empty_string


class RestorePhoneNumberRequest(TypedDict, closed=True):
    phone_number_id: "aws_sdk_chime.types.non_empty_string.NonEmptyString"
    """<p>The phone number.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RestorePhoneNumberRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RestorePhoneNumberRequest:
    out: RestorePhoneNumberRequest = {}  # type: ignore[typeddict-item]
    return out
