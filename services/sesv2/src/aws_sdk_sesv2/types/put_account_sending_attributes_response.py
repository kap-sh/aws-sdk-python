"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountSendingAttributesResponse``."""

from typing_extensions import TypedDict


class PutAccountSendingAttributesResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSendingAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutAccountSendingAttributesResponse:
    out: PutAccountSendingAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
