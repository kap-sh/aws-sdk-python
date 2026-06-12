"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_name
    import aws_sdk_bedrock_data_automation.types.data_automation_project_stage
    import aws_sdk_bedrock_data_automation.types.data_automation_project_type
    import aws_sdk_bedrock_data_automation.types.date_timestamp


class DataAutomationProjectSummary(TypedDict):
    project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    project_stage: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    project_type: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_type.DataAutomationProjectType"
    ]
    project_name: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_name.DataAutomationProjectName"
    ]
    creation_time: "aws_sdk_bedrock_data_automation.types.date_timestamp.DateTimestamp"


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectSummary) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "project_stage" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    if "project_type" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_type

        out["projectType"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_type.serialize_json(
                value["project_type"]
            )
        )
    if "project_name" in value:
        out["projectName"] = value["project_name"]
    import aws_sdk_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        aws_sdk_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    return out


def deserialize_json(data: dict) -> DataAutomationProjectSummary:
    out: DataAutomationProjectSummary = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError("DataAutomationProjectSummary.project_arn required")
    if "projectStage" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    if "projectType" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_type

        out["project_type"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_type.deserialize_json(
                data["projectType"]
            )
        )
    if "projectName" in data:
        out["project_name"] = data["projectName"]
    if "creationTime" in data:
        import aws_sdk_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            aws_sdk_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        raise DeserializationError(
            "DataAutomationProjectSummary.creation_time required"
        )
    return out
