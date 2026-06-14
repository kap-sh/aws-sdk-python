"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteBandwidthRateLimitOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn


class DeleteBandwidthRateLimitOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteBandwidthRateLimitOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteBandwidthRateLimitOutput:
    out: DeleteBandwidthRateLimitOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    return out
