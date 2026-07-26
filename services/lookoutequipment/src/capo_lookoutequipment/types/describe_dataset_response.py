"""Generated from Smithy shape ``com.amazonaws.lookoutequipment#DescribeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lookoutequipment.types.data_quality_summary
    import capo_lookoutequipment.types.dataset_arn
    import capo_lookoutequipment.types.dataset_name
    import capo_lookoutequipment.types.dataset_status
    import capo_lookoutequipment.types.iam_role_arn
    import capo_lookoutequipment.types.ingested_files_summary
    import capo_lookoutequipment.types.ingestion_input_configuration
    import capo_lookoutequipment.types.kms_key_arn
    import capo_lookoutequipment.types.synthesized_json_inline_data_schema
    import capo_lookoutequipment.types.timestamp


class DescribeDatasetResponse(TypedDict, closed=True):
    dataset_name: NotRequired["capo_lookoutequipment.types.dataset_name.DatasetName"]
    """<p>The name of the dataset being described. </p>"""
    dataset_arn: NotRequired["capo_lookoutequipment.types.dataset_arn.DatasetArn"]
    """<p>The Amazon Resource Name (ARN) of the dataset being described. </p>"""
    created_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Specifies the time the dataset was created in Lookout for Equipment. </p>"""
    last_updated_at: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p>Specifies the time the dataset was last updated, if it was. </p>"""
    status: NotRequired["capo_lookoutequipment.types.dataset_status.DatasetStatus"]
    """<p>Indicates the status of the dataset. </p>"""
    schema: NotRequired[
        "capo_lookoutequipment.types.synthesized_json_inline_data_schema.SynthesizedJsonInlineDataSchema"
    ]
    """<p>A JSON description of the data that is in each time series dataset, including names, column names, and data types. </p>"""
    server_side_kms_key_id: NotRequired[
        "capo_lookoutequipment.types.kms_key_arn.KmsKeyArn"
    ]
    """<p>Provides the identifier of the KMS key used to encrypt dataset data by Amazon Lookout for Equipment. </p>"""
    ingestion_input_configuration: NotRequired[
        "capo_lookoutequipment.types.ingestion_input_configuration.IngestionInputConfiguration"
    ]
    """<p>Specifies the S3 location configuration for the data input for the data ingestion job. </p>"""
    data_quality_summary: NotRequired[
        "capo_lookoutequipment.types.data_quality_summary.DataQualitySummary"
    ]
    """<p> Gives statistics associated with the given dataset for the latest successful associated ingestion job id. These statistics primarily relate to quantifying incorrect data such as MissingCompleteSensorData, MissingSensorData, UnsupportedDateFormats, InsufficientSensorData, and DuplicateTimeStamps. </p>"""
    ingested_files_summary: NotRequired[
        "capo_lookoutequipment.types.ingested_files_summary.IngestedFilesSummary"
    ]
    """<p>IngestedFilesSummary associated with the given dataset for the latest successful associated ingestion job id. </p>"""
    role_arn: NotRequired["capo_lookoutequipment.types.iam_role_arn.IamRoleArn"]
    """<p> The Amazon Resource Name (ARN) of the IAM role that you are using for this the data ingestion job. </p>"""
    data_start_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Indicates the earliest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset. </p>"""
    data_end_time: NotRequired["capo_lookoutequipment.types.timestamp.Timestamp"]
    """<p> Indicates the latest timestamp corresponding to data that was successfully ingested during the most recent ingestion of this particular dataset. </p>"""
    source_dataset_arn: NotRequired[
        "capo_lookoutequipment.types.dataset_arn.DatasetArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the source dataset from which the current data being described was imported from.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeDatasetResponse) -> dict:
    out: dict = {}
    if "dataset_name" in value:
        out["DatasetName"] = value["dataset_name"]
    if "dataset_arn" in value:
        out["DatasetArn"] = value["dataset_arn"]
    if "created_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["CreatedAt"] = capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
            value["created_at"]
        )
    if "last_updated_at" in value:
        import capo_lookoutequipment.types.timestamp

        out["LastUpdatedAt"] = (
            capo_lookoutequipment.types.timestamp.serialize_aws_json_1_0(
                value["last_updated_at"]
            )
        )
    if "status" in value:
        import capo_lookoutequipment.types.dataset_status

        out["Status"] = (
            capo_lookoutequipment.types.dataset_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "schema" in value:
        out["Schema"] = value["schema"]
    if "server_side_kms_key_id" in value:
        out["ServerSideKmsKeyId"] = value["server_side_kms_key_id"]
    if "ingestion_input_configuration" in value:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["IngestionInputConfiguration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.serialize_aws_json_1_0(
                value["ingestion_input_configuration"]
            )
        )
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
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
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


def deserialize_aws_json_1_0(data: dict) -> DescribeDatasetResponse:
    out: DescribeDatasetResponse = {}  # type: ignore[typeddict-item]
    if "DatasetName" in data:
        out["dataset_name"] = data["DatasetName"]
    if "DatasetArn" in data:
        out["dataset_arn"] = data["DatasetArn"]
    if "CreatedAt" in data:
        import capo_lookoutequipment.types.timestamp

        out["created_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_lookoutequipment.types.timestamp

        out["last_updated_at"] = (
            capo_lookoutequipment.types.timestamp.deserialize_aws_json_1_0(
                data["LastUpdatedAt"]
            )
        )
    if "Status" in data:
        import capo_lookoutequipment.types.dataset_status

        out["status"] = (
            capo_lookoutequipment.types.dataset_status.deserialize_aws_json_1_0(
                data["Status"]
            )
        )
    if "Schema" in data:
        out["schema"] = data["Schema"]
    if "ServerSideKmsKeyId" in data:
        out["server_side_kms_key_id"] = data["ServerSideKmsKeyId"]
    if "IngestionInputConfiguration" in data:
        import capo_lookoutequipment.types.ingestion_input_configuration

        out["ingestion_input_configuration"] = (
            capo_lookoutequipment.types.ingestion_input_configuration.deserialize_aws_json_1_0(
                data["IngestionInputConfiguration"]
            )
        )
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
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
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
