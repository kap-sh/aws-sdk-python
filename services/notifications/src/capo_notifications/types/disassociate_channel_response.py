"""Generated from Smithy shape ``com.amazonaws.notifications#DisassociateChannelResponse``."""

from typing_extensions import TypedDict


class DisassociateChannelResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: DisassociateChannelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DisassociateChannelResponse:
    out: DisassociateChannelResponse = {}  # type: ignore[typeddict-item]
    return out
