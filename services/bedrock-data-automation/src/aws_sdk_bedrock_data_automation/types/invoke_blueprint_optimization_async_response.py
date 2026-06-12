"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InvokeBlueprintOptimizationAsyncResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn


class InvokeBlueprintOptimizationAsyncResponse(TypedDict):
    invocation_arn: "aws_sdk_bedrock_data_automation.types.blueprint_optimization_invocation_arn.BlueprintOptimizationInvocationArn"
    """ARN of the blueprint optimization job"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeBlueprintOptimizationAsyncResponse) -> dict:
    out: dict = {}
    out["invocationArn"] = value["invocation_arn"]
    return out


def deserialize_json(data: dict) -> InvokeBlueprintOptimizationAsyncResponse:
    out: InvokeBlueprintOptimizationAsyncResponse = {}  # type: ignore[typeddict-item]
    if "invocationArn" in data:
        out["invocation_arn"] = data["invocationArn"]
    else:
        raise DeserializationError(
            "InvokeBlueprintOptimizationAsyncResponse.invocation_arn required"
        )
    return out
