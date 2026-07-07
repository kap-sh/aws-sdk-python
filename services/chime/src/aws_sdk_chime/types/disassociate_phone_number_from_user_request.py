"""Generated from Smithy shape ``com.amazonaws.chime#DisassociatePhoneNumberFromUserRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import aws_sdk_chime.types.string


class DisassociatePhoneNumberFromUserRequest(TypedDict, closed=True):
    account_id: "aws_sdk_chime.types.string.String"
    """<p>The Amazon Chime account ID.</p>"""
    user_id: "aws_sdk_chime.types.string.String"
    """<p>The user ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePhoneNumberFromUserRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociatePhoneNumberFromUserRequest:
    out: DisassociatePhoneNumberFromUserRequest = {}  # type: ignore[typeddict-item]
    return out
