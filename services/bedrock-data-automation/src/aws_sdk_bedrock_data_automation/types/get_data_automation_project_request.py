"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage


class GetDataAutomationProjectRequest(TypedDict):
    project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    """ARN generated at the server side when a DataAutomationProject is created"""
    project_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    """Optional field to delete a specific DataAutomationProject stage"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationProjectRequest) -> dict:
    out: dict = {}
    if "project_stage" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataAutomationProjectRequest:
    out: GetDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectStage" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    return out
