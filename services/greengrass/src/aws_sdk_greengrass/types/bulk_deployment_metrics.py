"""Generated from Smithy shape ``com.amazonaws.greengrass#BulkDeploymentMetrics``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_greengrass.types.__integer


class BulkDeploymentMetrics(TypedDict, closed=True):
    invalid_input_records: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The total number of records that returned a non-retryable error. For example, this can occur if a group record from the input file uses an invalid format or specifies a nonexistent group version, or if the execution role doesn't grant permission to deploy a group or group version."""
    records_processed: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The total number of group records from the input file that have been processed so far, or attempted."""
    retry_attempts: NotRequired["aws_sdk_greengrass.types.__integer.__integer"]
    """The total number of deployment attempts that returned a retryable error. For example, a retry is triggered if the attempt to deploy a group returns a throttling error. ''StartBulkDeployment'' retries a group deployment up to five times."""


# --- restJson1 ser/de ---
def serialize_json(value: BulkDeploymentMetrics) -> dict:
    out: dict = {}
    if "invalid_input_records" in value:
        out["InvalidInputRecords"] = value["invalid_input_records"]
    if "records_processed" in value:
        out["RecordsProcessed"] = value["records_processed"]
    if "retry_attempts" in value:
        out["RetryAttempts"] = value["retry_attempts"]
    return out


def deserialize_json(data: dict) -> BulkDeploymentMetrics:
    out: BulkDeploymentMetrics = {}  # type: ignore[typeddict-item]
    if "InvalidInputRecords" in data:
        out["invalid_input_records"] = data["InvalidInputRecords"]
    if "RecordsProcessed" in data:
        out["records_processed"] = data["RecordsProcessed"]
    if "RetryAttempts" in data:
        out["retry_attempts"] = data["RetryAttempts"]
    return out
