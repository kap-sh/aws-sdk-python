"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateBlueprintRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_name
    import aws_sdk_bedrock_data_automation.types.blueprint_schema
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.client_token
    import aws_sdk_bedrock_data_automation.types.encryption_configuration
    import aws_sdk_bedrock_data_automation.types.tag_list
    import aws_sdk_bedrock_data_automation.types.type


class CreateBlueprintRequest(TypedDict):
    blueprint_name: "aws_sdk_bedrock_data_automation.types.blueprint_name.BlueprintName"
    type: "aws_sdk_bedrock_data_automation.types.type.Type"
    blueprint_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    schema: "aws_sdk_bedrock_data_automation.types.blueprint_schema.BlueprintSchema"
    client_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.client_token.ClientToken"
    ]
    encryption_configuration: NotRequired[
        "aws_sdk_bedrock_data_automation.types.encryption_configuration.EncryptionConfiguration"
    ]
    tags: NotRequired["aws_sdk_bedrock_data_automation.types.tag_list.TagList"]


# --- restJson1 ser/de ---
def serialize_json(value: CreateBlueprintRequest) -> dict:
    out: dict = {}
    out["blueprintName"] = value["blueprint_name"]
    import aws_sdk_bedrock_data_automation.types.type

    out["type"] = aws_sdk_bedrock_data_automation.types.type.serialize_json(
        value["type"]
    )
    if "blueprint_stage" in value:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    out["schema"] = value["schema"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "encryption_configuration" in value:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryptionConfiguration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.serialize_json(
                value["encryption_configuration"]
            )
        )
    if "tags" in value:
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateBlueprintRequest:
    out: CreateBlueprintRequest = {}  # type: ignore[typeddict-item]
    if "blueprintName" in data:
        out["blueprint_name"] = data["blueprintName"]
    else:
        raise DeserializationError("CreateBlueprintRequest.blueprint_name required")
    if "type" in data:
        import aws_sdk_bedrock_data_automation.types.type

        out["type"] = aws_sdk_bedrock_data_automation.types.type.deserialize_json(
            data["type"]
        )
    else:
        raise DeserializationError("CreateBlueprintRequest.type required")
    if "blueprintStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    if "schema" in data:
        out["schema"] = data["schema"]
    else:
        raise DeserializationError("CreateBlueprintRequest.schema required")
    if "clientToken" in data:
        out["client_token"] = data["clientToken"]
    if "encryptionConfiguration" in data:
        import aws_sdk_bedrock_data_automation.types.encryption_configuration

        out["encryption_configuration"] = (
            aws_sdk_bedrock_data_automation.types.encryption_configuration.deserialize_json(
                data["encryptionConfiguration"]
            )
        )
    if "tags" in data:
        import aws_sdk_bedrock_data_automation.types.tag_list

        out["tags"] = aws_sdk_bedrock_data_automation.types.tag_list.deserialize_json(
            data["tags"]
        )
    return out
