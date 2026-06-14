"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeAvailabilityMonitorTestInput``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn


class DescribeAvailabilityMonitorTestInput(TypedDict):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeAvailabilityMonitorTestInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeAvailabilityMonitorTestInput:
    out: DescribeAvailabilityMonitorTestInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError(
            "DescribeAvailabilityMonitorTestInput.gateway_arn required"
        )
    return out
