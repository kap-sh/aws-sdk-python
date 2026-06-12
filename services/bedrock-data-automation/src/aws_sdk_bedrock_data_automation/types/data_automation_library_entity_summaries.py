"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryEntitySummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summary

DataAutomationLibraryEntitySummaries: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summary.DataAutomationLibraryEntitySummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryEntitySummaries) -> list:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationLibraryEntitySummaries:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summary

    out: DataAutomationLibraryEntitySummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.data_automation_library_entity_summary.deserialize_json(
                item
            )
        )
    return out
