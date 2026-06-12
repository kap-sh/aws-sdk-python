"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryIngestionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary

DataAutomationLibraryIngestionJobSummaries: TypeAlias = list[
    "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.DataAutomationLibraryIngestionJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryIngestionJobSummaries) -> list:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary

    out: list = []
    for item in value:
        out.append(
            aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationLibraryIngestionJobSummaries:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary

    out: DataAutomationLibraryIngestionJobSummaries = []
    for item in data:
        out.append(
            aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.deserialize_json(
                item
            )
        )
    return out
