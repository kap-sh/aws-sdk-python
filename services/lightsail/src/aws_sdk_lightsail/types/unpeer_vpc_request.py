"""Generated from Smithy shape ``com.amazonaws.lightsail#UnpeerVpcRequest``."""

from typing_extensions import TypedDict


class UnpeerVpcRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UnpeerVpcRequest) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(data: dict) -> UnpeerVpcRequest:
    out: UnpeerVpcRequest = {}  # type: ignore[typeddict-item]
    return out
