"""Generated from Smithy shape ``com.amazonaws.mediaconvert#GetPolicyRequest``."""

from typing_extensions import TypedDict


class GetPolicyRequest(TypedDict, closed=True):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetPolicyRequest:
    out: GetPolicyRequest = {}  # type: ignore[typeddict-item]
    return out
