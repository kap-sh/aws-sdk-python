"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationProjectResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project


class GetDataAutomationProjectResponse(TypedDict, closed=True):
    project: "capo_bedrock_data_automation.types.data_automation_project.DataAutomationProject"


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationProjectResponse) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.data_automation_project

    out["project"] = (
        capo_bedrock_data_automation.types.data_automation_project.serialize_json(
            value["project"]
        )
    )
    return out


def deserialize_json(data: dict) -> GetDataAutomationProjectResponse:
    out: GetDataAutomationProjectResponse = {}  # type: ignore[typeddict-item]
    if "project" in data:
        import capo_bedrock_data_automation.types.data_automation_project

        out["project"] = (
            capo_bedrock_data_automation.types.data_automation_project.deserialize_json(
                data["project"]
            )
        )
    else:
        raise DeserializationError("GetDataAutomationProjectResponse.project required")
    return out
