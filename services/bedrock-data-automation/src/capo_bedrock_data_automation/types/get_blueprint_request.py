"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetBlueprintRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.blueprint_version


class GetBlueprintRequest(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    blueprint_version: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    """Optional field to get a specific Blueprint version"""
    blueprint_stage: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    """Optional field to get a specific Blueprint stage"""


# --- restJson1 ser/de ---
def serialize_json(value: GetBlueprintRequest) -> dict:
    out: dict = {}
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "blueprint_stage" in value:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetBlueprintRequest:
    out: GetBlueprintRequest = {}  # type: ignore[typeddict-item]
    if "blueprintVersion" in data:
        out["blueprint_version"] = data["blueprintVersion"]
    if "blueprintStage" in data:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    return out
