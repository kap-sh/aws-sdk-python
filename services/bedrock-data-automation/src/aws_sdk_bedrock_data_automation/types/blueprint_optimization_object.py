"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintOptimizationObject``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_stage


class BlueprintOptimizationObject(TypedDict, closed=True):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """Arn of blueprint."""
    stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    """Stage of blueprint."""


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintOptimizationObject) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    if "stage" in value:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> BlueprintOptimizationObject:
    out: BlueprintOptimizationObject = {}  # type: ignore[typeddict-item]
    if "blueprintArn" in data:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        raise DeserializationError("BlueprintOptimizationObject.blueprint_arn required")
    if "stage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["stage"]
            )
        )
    return out
