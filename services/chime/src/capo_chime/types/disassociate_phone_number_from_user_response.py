"""Generated from Smithy shape ``com.amazonaws.chime#DisassociatePhoneNumberFromUserResponse``."""

from typing_extensions import TypedDict


class DisassociatePhoneNumberFromUserResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociatePhoneNumberFromUserResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociatePhoneNumberFromUserResponse:
    out: DisassociatePhoneNumberFromUserResponse = {}  # type: ignore[typeddict-item]
    return out
