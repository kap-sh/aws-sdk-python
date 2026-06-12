"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationProjectSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_summary

DataAutomationProjectSummaries: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.data_automation_project_summary.DataAutomationProjectSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationProjectSummaries) -> list:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.data_automation_project_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationProjectSummaries:
    import aws_sdk_bedrock_data_automation.types.data_automation_project_summary

    out: DataAutomationProjectSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.data_automation_project_summary.deserialize_json(
                item
            )
        )
    return out
