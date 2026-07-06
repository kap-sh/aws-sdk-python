"""Generated from Smithy shape ``com.amazonaws.connect#SendOutboundEmailResponse``."""

from typing_extensions import TypedDict


class SendOutboundEmailResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: SendOutboundEmailResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> SendOutboundEmailResponse:
    out: SendOutboundEmailResponse = {}  # type: ignore[typeddict-item]
    return out
