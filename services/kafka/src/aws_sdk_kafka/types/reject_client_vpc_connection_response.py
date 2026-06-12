"""Generated from Smithy shape ``com.amazonaws.kafka#RejectClientVpcConnectionResponse``."""

from typing import TypedDict


class RejectClientVpcConnectionResponse(TypedDict):
    pass


# --- restJson1 ser/de ---
def serialize_json(value: RejectClientVpcConnectionResponse) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> RejectClientVpcConnectionResponse:
    out: RejectClientVpcConnectionResponse = {}  # type: ignore[typeddict-item]
    return out
