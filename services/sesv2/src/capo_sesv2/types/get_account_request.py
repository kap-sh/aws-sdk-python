"""Generated from Smithy shape ``com.amazonaws.sesv2#GetAccountRequest``."""

from typing_extensions import TypedDict


class GetAccountRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetAccountRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetAccountRequest:
    out: GetAccountRequest = {}  # type: ignore[typeddict-item]
    return out
