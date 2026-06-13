"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomationruntime#Blueprint``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation_runtime.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation_runtime.types.blueprint_arn
    import aws_sdk_bedrock_data_automation_runtime.types.blueprint_stage
    import aws_sdk_bedrock_data_automation_runtime.types.blueprint_version


class Blueprint(TypedDict):
    blueprint_arn: (
        "aws_sdk_bedrock_data_automation_runtime.types.blueprint_arn.BlueprintArn"
    )
    """Arn of blueprint."""
    version: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.blueprint_version.BlueprintVersion"
    ]
    """Version of blueprint."""
    stage: NotRequired[
        "aws_sdk_bedrock_data_automation_runtime.types.blueprint_stage.BlueprintStage"
    ]
    """Stage of blueprint."""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Blueprint) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    if "version" in value:
        out["version"] = value["version"]
    if "stage" in value:
        import aws_sdk_bedrock_data_automation_runtime.types.blueprint_stage

        out["stage"] = (
            aws_sdk_bedrock_data_automation_runtime.types.blueprint_stage.serialize_aws_json_1_1(
                value["stage"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Blueprint:
    out: Blueprint = {}  # type: ignore[typeddict-item]
    if "blueprintArn" in data:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        raise DeserializationError("Blueprint.blueprint_arn required")
    if "version" in data:
        out["version"] = data["version"]
    if "stage" in data:
        import aws_sdk_bedrock_data_automation_runtime.types.blueprint_stage

        out["stage"] = (
            aws_sdk_bedrock_data_automation_runtime.types.blueprint_stage.deserialize_aws_json_1_1(
                data["stage"]
            )
        )
    return out
