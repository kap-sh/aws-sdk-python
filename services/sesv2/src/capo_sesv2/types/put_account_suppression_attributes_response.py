"""Generated from Smithy shape ``com.amazonaws.sesv2#PutAccountSuppressionAttributesResponse``."""

from typing_extensions import TypedDict


class PutAccountSuppressionAttributesResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutAccountSuppressionAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutAccountSuppressionAttributesResponse:
    out: PutAccountSuppressionAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
