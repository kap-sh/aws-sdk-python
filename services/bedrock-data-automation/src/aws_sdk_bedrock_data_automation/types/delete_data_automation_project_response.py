"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteDataAutomationProjectResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_project_status


class DeleteDataAutomationProjectResponse(TypedDict):
    project_arn: "aws_sdk_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    status: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_project_status.DataAutomationProjectStatus"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataAutomationProjectResponse) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    if "status" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_status.serialize_json(
                value["status"]
            )
        )
    return out


def deserialize_json(data: dict) -> DeleteDataAutomationProjectResponse:
    out: DeleteDataAutomationProjectResponse = {}  # type: ignore[typeddict-item]
    if "projectArn" in data:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError(
            "DeleteDataAutomationProjectResponse.project_arn required"
        )
    if "status" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_project_status

        out["status"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_project_status.deserialize_json(
                data["status"]
            )
        )
    return out
