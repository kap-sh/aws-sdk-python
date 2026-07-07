"""Generated from Smithy shape ``com.amazonaws.lightsail#PeerVpcRequest``."""

from typing_extensions import TypedDict


class PeerVpcRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PeerVpcRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> PeerVpcRequest:
    out: PeerVpcRequest = {}  # type: ignore[typeddict-item]
    return out
