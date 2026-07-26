"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DeleteDataAutomationProjectRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_project_arn


class DeleteDataAutomationProjectRequest(TypedDict, closed=True):
    project_arn: "capo_bedrock_data_automation.types.data_automation_project_arn.DataAutomationProjectArn"
    """ARN generated at the server side when a DataAutomationProject is created"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataAutomationProjectRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteDataAutomationProjectRequest:
    out: DeleteDataAutomationProjectRequest = {}  # type: ignore[typeddict-item]
    return out
