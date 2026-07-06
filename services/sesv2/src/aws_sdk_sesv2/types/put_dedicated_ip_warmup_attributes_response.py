"""Generated from Smithy shape ``com.amazonaws.sesv2#PutDedicatedIpWarmupAttributesResponse``."""

from typing_extensions import TypedDict


class PutDedicatedIpWarmupAttributesResponse(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: PutDedicatedIpWarmupAttributesResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> PutDedicatedIpWarmupAttributesResponse:
    out: PutDedicatedIpWarmupAttributesResponse = {}  # type: ignore[typeddict-item]
    return out
