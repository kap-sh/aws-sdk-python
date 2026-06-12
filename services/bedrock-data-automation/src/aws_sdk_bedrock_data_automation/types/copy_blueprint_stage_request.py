"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CopyBlueprintStageRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.client_token


class CopyBlueprintStageRequest(TypedDict):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """Blueprint to be copied"""
    source_stage: "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    """Source stage to copy from"""
    target_stage: "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    """Target stage to copy to"""
    client_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
    ]
    """Client token for idempotency"""


# --- restJson1 ser/de ---
def serialize_json(value: CopyBlueprintStageRequest) -> dict:
    out: dict = {}
    import aws_sdk_bedrock_data_automation.types.blueprint_stage

    out["sourceStage"] = (
        aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
            value["source_stage"]
        )
    )
    import aws_sdk_bedrock_data_automation.types.blueprint_stage

    out["targetStage"] = (
        aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
            value["target_stage"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> CopyBlueprintStageRequest:
    out: CopyBlueprintStageRequest = {}  # type: ignore[typeddict-item]
    if "sourceStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["source_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["sourceStage"]
            )
        )
    else:
        raise DeserializationError("CopyBlueprintStageRequest.source_stage required")
    if "targetStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["target_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["targetStage"]
            )
        )
    else:
        raise DeserializationError("CopyBlueprintStageRequest.target_stage required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    return out
