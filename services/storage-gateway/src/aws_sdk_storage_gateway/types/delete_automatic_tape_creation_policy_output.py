"""Generated from Smithy shape ``com.amazonaws.storagegateway#DeleteAutomaticTapeCreationPolicyOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_storage_gateway.types.gateway_arn


class DeleteAutomaticTapeCreationPolicyOutput(TypedDict):
    gateway_arn: NotRequired["aws_sdk_storage_gateway.types.gateway_arn.GatewayARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAutomaticTapeCreationPolicyOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAutomaticTapeCreationPolicyOutput:
    out: DeleteAutomaticTapeCreationPolicyOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    return out
