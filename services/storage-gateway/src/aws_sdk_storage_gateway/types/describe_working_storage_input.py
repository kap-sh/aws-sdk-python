"""Generated from Smithy shape ``com.amazonaws.storagegateway#DescribeWorkingStorageInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_storage_gateway.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn


class DescribeWorkingStorageInput(TypedDict, closed=True):
    gateway_arn: "aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeWorkingStorageInput) -> dict:
    out: dict = {}
    out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeWorkingStorageInput:
    out: DescribeWorkingStorageInput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    else:
        raise DeserializationError("DescribeWorkingStorageInput.gateway_arn required")
    return out
