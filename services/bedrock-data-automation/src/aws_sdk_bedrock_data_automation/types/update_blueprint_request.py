"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateBlueprintRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_schema
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.encryption_configuration


class UpdateBlueprintRequest(TypedDict):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    """ARN generated at the server side when a Blueprint is created"""
    schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema"
    blueprint_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    encryption_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBlueprintRequest) -> dict:
    out: dict = {}
    out["schema"] = value["schema"]
    if "blueprint_stage" in value:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    if "encryption_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateBlueprintRequest:
    out: UpdateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if "schema" in data:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("UpdateBlueprintRequest.schema required")
    if "blueprintStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    if "encryptionConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    return out
