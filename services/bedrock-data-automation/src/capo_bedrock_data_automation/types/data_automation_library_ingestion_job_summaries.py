"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#DataAutomationLibraryIngestionJobSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary

DataAutomationLibraryIngestionJobSummaries: TypeAlias = list[
    "capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.DataAutomationLibraryIngestionJobSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: DataAutomationLibraryIngestionJobSummaries) -> list:
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary

    out: list = []
    for item in value:
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> DataAutomationLibraryIngestionJobSummaries:
    import capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary

    out: DataAutomationLibraryIngestionJobSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_bedrock_data_automation.types.data_automation_library_ingestion_job_summary.deserialize_json(
                item
            )
        )
    return out
