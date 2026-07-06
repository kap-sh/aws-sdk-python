"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#CreateDataAutomationProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage
    import aws_sdk_bedrock_data_automation.types.data_automation_project_status


class CreateDataAutomationProjectResponse(TypedDict, closed=True):
    project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    project_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    status: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_status.DataAutomationProjectStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: CreateDataAutomationProjectResponse) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "project_stage" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "status" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateDataAutomationProjectResponse:
    out: CreateDataAutomationProjectResponse = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError(
            "CreateDataAutomationProjectResponse.project_arn required"
        )
    if "projectStage" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    if "status" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_status.deserialize_json(
                data["status"]
            )
        )
    return out
