"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeDataIngestionJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.bounded_length_string
    import capo_lookoutequipment.types.data_quality_summary
    import capo_lookoutequipment.types.data_size_in_bytes
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.ingested_files_summary
    import capo_lookoutequipment.types.ingestion_input_configuration
    import capo_lookoutequipment.types.ingestion_job_id
    import capo_lookoutequipment.types.ingestion_job_status
    import capo_lookoutequipment.types.timestamp


class DescribeDataIngestionJobResponse(TypedDict, closed=True):
    job_id: NotRequired["capo_lookoutequipment.types.ingestion_job_id.IngestionJobId"]
    """<p>Indicates the job ID of the data ingestion job. </p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resource Name (ARN) of the dataset being used in the data ingestion job. </p>"""
    ingestion_input_configuration: NotRequired[
        "capo_lookoutequipment.types.ingestion_input_configuration.IngestionInputConfiguration"
    ]
    """<p>Specifies the S3 location configuration for the data input for the data ingestion job. </p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p>The Amazon Resource Name (ARN) of an IAM role with permission to access the data source being ingested. </p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>The time at which the data ingestion job was created. </p>"""
    status: NotRequired[
        "capo_lookoutequipment.types.ingestion_job_status.IngestionJobStatus"
    ]
    """<p>Indicates the status of the <code>DataIngestionJob</code> operation. </p>"""
    failed_reason: NotRequired[
        "capo_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p>Specifies the reason for failure when a data ingestion job has failed. </p>"""
    data_quality_summary: NotRequired[
        "capo_lookoutequipment.types.data_quality_summary.DataQualitySummary"
    ]
    """<p> Gives statistics about a completed ingestion job. These statistics primarily relate to quantifying incorrect data such as MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, and DuplicateTimeStamps. </p>"""
    ingested_files_summary: NotRequired[
        "capo_lookoutequipment.types.ingested_files_summary.IngestedFilesSummary"
    ]
    status_detail: NotRequired[
        "capo_lookoutequipment.types.bounded_length_string.BoundedLengthString"
    ]
    """<p> Provides details about status of the ingestion job that is currently in progress. </p>"""
    ingested_data_size: NotRequired[
        "capo_lookoutequipment.types.data_size_in_bytes.DataSizeInBytes"
    ]
    """<p> Indicates the size of the ingested dataset. </p>"""
    data_start_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Indicates the earliest timestamp corresponding to data that was successfully ingested during this specific ingestion job. </p>"""
    data_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Indicates the latest timestamp corresponding to data that was successfully ingested during this specific ingestion job. </p>"""
    source_dataset_arn: NotRequired[
        "capo_lookoutequipment.types.dataset_arn.DatasetArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source dataset from which the data used for the data ingestion job was imported from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDataIngestionJobResponse) -> dict:
    out: dict = {}
    if "job_id" in value:
        out["JobId"] = value["job_id"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "ingestion_input_configuration" in value:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["IngestionInputConfiguration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.serialize_aws_json_1_0(
                value["ingestion_input_configuration"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "status" in value:
        import capo_lookoutequipment.types.ingestion_job_status

        out["Status"] = (
            capo_lookoutequipment.types.ingestion_job_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "failed_reason" in value:
        out["FailedReason"] = value["failed_reason"]
    if "data_quality_summary" in value:
        import capo_lookoutequipment.types.data_quality_summary

        out["DataQualitySummary"] = (
            capo_lookoutequipment.types.data_quality_summary.serialize_aws_json_1_0(
                value["data_quality_summary"]
            )
        )
    if "ingested_files_summary" in value:
        import capo_lookoutequipment.types.ingested_files_summary

        out["IngestedFilesSummary"] = (
            capo_lookoutequipment.types.ingested_files_summary.serialize_aws_json_1_0(
                value["ingested_files_summary"]
            )
        )
    if "status_detail" in value:
        out["StatusDetail"] = value["status_detail"]
    if "ingested_data_size" in value:
        out["IngestedDataSize"] = value["ingested_data_size"]
    if "data_start_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["DataStartTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_start_time"]
            )
        )
    if "data_end_time" in value:
        import capo_lookoutequipment.types.timestamp

        out["DataEndTime"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["data_end_time"]
            )
        )
    if "source_dataset_arn" in value:
        out["SourceDatasetArn"] = value["source_dataset_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeDataIngestionJobResponse:
    out: DescribeDataIngestionJobResponse = {}  # type: ignore[typeddict-item]
    if "JobId" in data:
        out["job_id"] = data["JobId"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "IngestionInputConfiguration" in data:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["ingestion_input_configuration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.deserialize_aws_json_1_0(
                data["IngestionInputConfiguration"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "CreatedAt" in data:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "Status" in data:
        import capo_lookoutequipment.types.ingestion_job_status

        out["status"] = (
            capo_lookoutequipment.types.ingestion_job_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "FailedReason" in data:
        out["failed_reason"] = data["FailedReason"]
    if "DataQualitySummary" in data:
        import capo_lookoutequipment.types.data_quality_summary

        out["data_quality_summary"] = (
            capo_lookoutequipment.types.data_quality_summary.deserialize_aws_json_1_0(
                data["DataQualitySummary"]
            )
        )
    if "IngestedFilesSummary" in data:
        import capo_lookoutequipment.types.ingested_files_summary

        out["ingested_files_summary"] = (
            capo_lookoutequipment.types.ingested_files_summary.deserialize_aws_json_1_0(
                data["IngestedFilesSummary"]
            )
        )
    if "StatusDetail" in data:
        out["status_detail"] = data["StatusDetail"]
    if "IngestedDataSize" in data:
        out["ingested_data_size"] = data["IngestedDataSize"]
    if "DataStartTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["data_start_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataStartTime"]
            )
        )
    if "DataEndTime" in data:
        import capo_lookoutequipment.types.timestamp

        out["data_end_time"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["DataEndTime"]
            )
        )
    if "SourceDatasetArn" in data:
        out["source_dataset_arn"] = data["SourceDatasetArn"]
    return out
