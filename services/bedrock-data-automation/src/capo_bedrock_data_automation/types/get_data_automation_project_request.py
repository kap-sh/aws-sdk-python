"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_arn
    import capo_bedrock_data_automation.types.data_automation_project_stage


class GetDataAutomationProjectRequest(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    """ARN generated at the server side when a DataAutomationProject is created"""
    project_stage: NotRequired[
        "capo_bedrock_data_automation.types.data_automation_project_stage.DataAutomationProjectStage"
    ]
    """Optional field to delete a specific DataAutomationProject stage"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationProjectRequest) -> dict:
    out: dict = {}
    if "project_stage" in value:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["projectStage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.serialize_json(
                value["project_stage"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataAutomationProjectRequest:
    out: GetDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    if "projectStage" in data:
        import capo_bedrock_data_automation.types.data_automation_project_stage

        out["project_stage"] = (
            capo_bedrock_data_automation.types.data_automation_project_stage.deserialize_json(
                data["projectStage"]
            )
        )
    return out
