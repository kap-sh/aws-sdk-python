"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#CloseTunnelResponse``."""

from typing_extensions import TypedDict


class CloseTunnelResponse(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloseTunnelResponse) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> CloseTunnelResponse:
    out: CloseTunnelResponse = {}  # type: ignore[typeddict-item]
    return out
