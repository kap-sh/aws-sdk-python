"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryIngestionJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_arn
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn


class GetDataAutomationLibraryIngestionJobRequest(TypedDict):
    library_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_arn.DataAutomationLibraryArn"
    """ARN generated at the server side when a DataAutomationLibrary is created"""
    job_arn: "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn"
    """ARN of the DataAutomationLibraryIngestionJob"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryIngestionJobRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryIngestionJobRequest:
    out: GetDataAutomationLibraryIngestionJobRequest = {}  # type: ignore[typeddict-item]
    return out
