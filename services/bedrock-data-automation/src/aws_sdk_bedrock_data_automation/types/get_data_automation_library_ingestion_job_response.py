"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryIngestionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job


class GetDataAutomationLibraryIngestionJobResponse(TypedDict, closed=True):
    job: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job.DataAutomationLibraryIngestionJob"
    ]
    """Contains the information of a library ingestion job"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryIngestionJobResponse) -> dict:
    out: dict = {}
    if "job" in value:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job

        out["job"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job.serialize_json(
                value["job"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryIngestionJobResponse:
    out: GetDataAutomationLibraryIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if "job" in data:
        import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job

        out["job"] = (
            aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job.deserialize_json(
                data["job"]
            )
        )
    return out
