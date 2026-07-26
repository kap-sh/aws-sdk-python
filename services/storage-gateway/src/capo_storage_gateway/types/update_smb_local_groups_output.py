"""Generated from Smithy shape ``com.amazonaws.storagegateway#UpdateSMBLocalGroupsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_storage_gateway.types.gateway_arn


class UpdateSMBLocalGroupsOutput(TypedDict, closed=True):
    gateway_arn: NotRequired["capo_storage_gateway.types.gateway_arn.GatewayARN"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateSMBLocalGroupsOutput) -> dict:
    out: dict = {}
    if "gateway_arn" in value:
        out["GatewayARN"] = value["gateway_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateSMBLocalGroupsOutput:
    out: UpdateSMBLocalGroupsOutput = {}  # type: ignore[typeddict-item]
    if "GatewayARN" in data:
        out["gateway_arn"] = data["GatewayARN"]
    return out
