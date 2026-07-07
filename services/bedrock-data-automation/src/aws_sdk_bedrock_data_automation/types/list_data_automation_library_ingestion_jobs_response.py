"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListDataAutomationLibraryIngestionJobsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summaries
    import aws_sdk_bedrock_data_automation.types.next_token


class ListDataAutomationLibraryIngestionJobsResponse(TypedDict, closed=True):
    jobs: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summaries.DataAutomationLibraryIngestionJobSummaries"
    ]
    """List of data automation library ingestion jobs"""
    next_token: NotRequired[
        "aws_sdk_bedrock_data_automation.types.next_token.NextToken"
    ]
    """Pagination token for retrieving the next set of results"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataAutomationLibraryIngestionJobsResponse) -> dict:
    out: dict = {}
    if "jobs" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summaries

        out["jobs"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summaries.serialize_json(
                value["jobs"]
            )
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListDataAutomationLibraryIngestionJobsResponse:
    out: ListDataAutomationLibraryIngestionJobsResponse = {}  # type: ignore[typeddict-item]
    if "jobs" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summaries

        out["jobs"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_summaries.deserialize_json(
                data["jobs"]
            )
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
