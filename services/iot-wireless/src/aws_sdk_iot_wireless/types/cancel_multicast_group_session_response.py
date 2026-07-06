"""Generated from Smithy shape ``com.amazonaws.iotwireless#CancelMulticastGroupSessionResponse``."""

from typing_extensions import TypedDict


class CancelMulticastGroupSessionResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: CancelMulticastGroupSessionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> CancelMulticastGroupSessionResponse:
    out: CancelMulticastGroupSessionResponse = {}  # type: ignore[typeddict-item]
    return out
