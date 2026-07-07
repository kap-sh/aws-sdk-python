"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.blueprint_version


class BlueprintFilter(TypedDict, closed=True):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    blueprint_version: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    blueprint_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintFilter) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "blueprint_stage" in value:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> BlueprintFilter:
    out: BlueprintFilter = {}  # type: ignore[typeddict-item]
    if "blueprintArn" in data:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        raise DeserializationError("BlueprintFilter.blueprint_arn required")
    if "blueprintVersion" in data:
        out["blueprint_version"] = data["blueprintVersion"]
    if "blueprintStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    return out
