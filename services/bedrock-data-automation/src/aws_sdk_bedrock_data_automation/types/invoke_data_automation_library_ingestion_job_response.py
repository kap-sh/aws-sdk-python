"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InvokeDataAutomationLibraryIngestionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn


class InvokeDataAutomationLibraryIngestionJobResponse(TypedDict, closed=True):
    job_arn: NotRequired[
        "aws_sdk_bedrock_data_automation.types.data_automation_library_ingestion_job_arn.DataAutomationLibraryIngestionJobArn"
    ]
    """ARN of the DataAutomationLibraryIngestionJob"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeDataAutomationLibraryIngestionJobResponse) -> dict:
    out: dict = {}
    if "job_arn" in value:
        out["jobArn"] = value["job_arn"]
    return out


def deserialize_json(data: dict) -> InvokeDataAutomationLibraryIngestionJobResponse:
    out: InvokeDataAutomationLibraryIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if "jobArn" in data:
        out["job_arn"] = data["jobArn"]
    return out
