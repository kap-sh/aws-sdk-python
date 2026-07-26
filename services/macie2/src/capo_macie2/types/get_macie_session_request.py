"""Generated from Smithy shape ``com.amazonaws.macie2#GetMacieSessionRequest``."""

from typing_extensions import TypedDict


class GetMacieSessionRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetMacieSessionRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetMacieSessionRequest:
    out: GetMacieSessionRequest = {}  # type: ignore[typeddict-item]
    return out
