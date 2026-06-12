"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetBlueprintOptimizationStatusRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn


class GetBlueprintOptimizationStatusRequest(TypedDict):
    invocation_arn: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn"
    """Invocation arn."""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlueprintOptimizationStatusRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetBlueprintOptimizationStatusRequest:
    out: GetBlueprintOptimizationStatusRequest = {}  # type: ignore[typeddict-item]
    return out
