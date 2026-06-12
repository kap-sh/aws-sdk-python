"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.blueprint_arn
    import aws_sdk_bedrock_data_automation.types.blueprint_name
    import aws_sdk_bedrock_data_automation.types.blueprint_stage
    import aws_sdk_bedrock_data_automation.types.blueprint_version
    import aws_sdk_bedrock_data_automation.types.date_timestamp


class BlueprintSummary(TypedDict):
    blueprint_arn: "aws_sdk_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    blueprint_version: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    blueprint_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    blueprint_name: NotRequired[
        "aws_sdk_bedrock_data_automation.types.blueprint_name.BlueprintName"
    ]
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    last_modified_time: NotRequired[
        "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintSummary) -> dict:
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
    if "blueprint_name" in value:
        out["blueprintName"] = value["blueprint_name"]
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    if "last_modified_time" in value:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["lastModifiedTime"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BlueprintSummary:
    out: BlueprintSummary = {}  # type: ignore[typeddict-item]
    if "blueprintArn" in data:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        raise DeserializationError("BlueprintSummary.blueprint_arn required")
    if "blueprintVersion" in data:
        out["blueprint_version"] = data["blueprintVersion"]
    if "blueprintStage" in data:
        import aws_sdk_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            aws_sdk_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    if "blueprintName" in data:
        out["blueprint_name"] = data["blueprintName"]
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError("BlueprintSummary.creation_time required")
    if "lastModifiedTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out
