"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetDataSourceOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.aws_user_arn
    import aws_sdk_machine_learning.types.compute_statistics
    import aws_sdk_machine_learning.types.data_rearrangement
    import aws_sdk_machine_learning.types.data_schema
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.entity_name
    import aws_sdk_machine_learning.types.entity_status
    import aws_sdk_machine_learning.types.epoch_time
    import aws_sdk_machine_learning.types.long_type
    import aws_sdk_machine_learning.types.message
    import aws_sdk_machine_learning.types.presigned_s3_url
    import aws_sdk_machine_learning.types.rds_metadata
    import aws_sdk_machine_learning.types.redshift_metadata
    import aws_sdk_machine_learning.types.role_arn
    import aws_sdk_machine_learning.types.s3_url


class GetDataSourceOutput(TypedDict):
    data_source_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID assigned to the <code>DataSource</code> at creation. This value should be identical to the value of the <code>DataSourceId</code> in the request.</p>"""
    data_location_s3: NotRequired["aws_sdk_machine_learning.types.s3_url.S3Url"]
    """<p>The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).</p>"""
    data_rearrangement: NotRequired[
        "aws_sdk_machine_learning.types.data_rearrangement.DataRearrangement"
    ]
    """<p>A JSON string that represents the splitting and rearrangement requirement used when this <code>DataSource</code> was created.</p>"""
    created_by_iam_user: NotRequired[
        "aws_sdk_machine_learning.types.aws_user_arn.AwsUserArn"
    ]
    """<p>The AWS user account from which the <code>DataSource</code> was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.</p>"""
    created_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the <code>DataSource</code> was created. The time is expressed in epoch time.</p>"""
    last_updated_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time of the most recent edit to the <code>DataSource</code>. The time is expressed in epoch time.</p>"""
    data_size_in_bytes: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    """<p>The total size of observations in the data files.</p>"""
    number_of_files: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    """<p>The number of data files referenced by the <code>DataSource</code>.</p>"""
    name: NotRequired["aws_sdk_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>DataSource</code>.</p>"""
    status: NotRequired["aws_sdk_machine_learning.types.entity_status.EntityStatus"]
    """<p>The current status of the <code>DataSource</code>. This element can have one of the following values:</p> <ul> <li> <p> <code>PENDING</code> - Amazon ML submitted a request to create a <code>DataSource</code>.</p> </li> <li> <p> <code>INPROGRESS</code> - The creation process is underway.</p> </li> <li> <p> <code>FAILED</code> - The request to create a <code>DataSource</code> did not run to completion. It is not usable.</p> </li> <li> <p> <code>COMPLETED</code> - The creation process completed successfully.</p> </li> <li> <p> <code>DELETED</code> - The <code>DataSource</code> is marked as deleted. It is not usable.</p> </li> </ul>"""
    log_uri: NotRequired[
        "aws_sdk_machine_learning.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>A link to the file containing logs of <code>CreateDataSourceFrom*</code> operations.</p>"""
    message: NotRequired["aws_sdk_machine_learning.types.message.Message"]
    """<p>The user-supplied description of the most recent details about creating the <code>DataSource</code>.</p>"""
    redshift_metadata: NotRequired[
        "aws_sdk_machine_learning.types.redshift_metadata.RedshiftMetadata"
    ]
    rds_metadata: NotRequired["aws_sdk_machine_learning.types.rds_metadata.RDSMetadata"]
    role_arn: NotRequired["aws_sdk_machine_learning.types.role_arn.RoleARN"]
    compute_statistics: (
        "aws_sdk_machine_learning.types.compute_statistics.ComputeStatistics"
    )
    """<p> The parameter is <code>true</code> if statistics need to be generated from the observation data. </p>"""
    compute_time: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    """<p>The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the <code>DataSource</code>, normalized and scaled on computation resources. <code>ComputeTime</code> is only available if the <code>DataSource</code> is in the <code>COMPLETED</code> state and the <code>ComputeStatistics</code> is set to true.</p>"""
    finished_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The epoch time when Amazon Machine Learning marked the <code>DataSource</code> as <code>COMPLETED</code> or <code>FAILED</code>. <code>FinishedAt</code> is only available when the <code>DataSource</code> is in the <code>COMPLETED</code> or <code>FAILED</code> state.</p>"""
    started_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The epoch time when Amazon Machine Learning marked the <code>DataSource</code> as <code>INPROGRESS</code>. <code>StartedAt</code> isn't available if the <code>DataSource</code> is in the <code>PENDING</code> state.</p>"""
    data_source_schema: NotRequired[
        "aws_sdk_machine_learning.types.data_schema.DataSchema"
    ]
    """<p>The schema used by all of the data files of this <code>DataSource</code>.</p> <p> <b>Note:</b> This parameter is provided as part of the verbose format.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetDataSourceOutput) -> dict:
    out: dict = {}
    if "data_source_id" in value:
        out["DataSourceId"] = value["data_source_id"]
    if "data_location_s3" in value:
        out["DataLocationS3"] = value["data_location_s3"]
    if "data_rearrangement" in value:
        out["DataRearrangement"] = value["data_rearrangement"]
    if "created_by_iam_user" in value:
        out["CreatedByIamUser"] = value["created_by_iam_user"]
    if "created_at" in value:
        import aws_sdk_machine_learning.types.epoch_time

        out["CreatedAt"] = (
            aws_sdk_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import aws_sdk_machine_learning.types.epoch_time

        out["LastUpdatedAt"] = (
            aws_sdk_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["last_updated_at"]
            )
        )
    if "data_size_in_bytes" in value:
        out["DataSizeInBytes"] = value["data_size_in_bytes"]
    if "number_of_files" in value:
        out["NumberOfFiles"] = value["number_of_files"]
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_machine_learning.types.entity_status

        out["Status"] = (
            aws_sdk_machine_learning.types.entity_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
    if "message" in value:
        out["Message"] = value["message"]
    if "redshift_metadata" in value:
        import aws_sdk_machine_learning.types.redshift_metadata

        out["RedshiftMetadata"] = (
            aws_sdk_machine_learning.types.redshift_metadata.serialize_aws_json_1_1(
                value["redshift_metadata"]
            )
        )
    if "rds_metadata" in value:
        import aws_sdk_machine_learning.types.rds_metadata

        out["RDSMetadata"] = (
            aws_sdk_machine_learning.types.rds_metadata.serialize_aws_json_1_1(
                value["rds_metadata"]
            )
        )
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    out["ComputeStatistics"] = value.get("compute_statistics", False)
    if "compute_time" in value:
        out["ComputeTime"] = value["compute_time"]
    if "finished_at" in value:
        import aws_sdk_machine_learning.types.epoch_time

        out["FinishedAt"] = (
            aws_sdk_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["finished_at"]
            )
        )
    if "started_at" in value:
        import aws_sdk_machine_learning.types.epoch_time

        out["StartedAt"] = (
            aws_sdk_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["started_at"]
            )
        )
    if "data_source_schema" in value:
        out["DataSourceSchema"] = value["data_source_schema"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetDataSourceOutput:
    out: GetDataSourceOutput = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "DataLocationS3" in data:
        out["data_location_s3"] = data["DataLocationS3"]
    if "DataRearrangement" in data:
        out["data_rearrangement"] = data["DataRearrangement"]
    if "CreatedByIamUser" in data:
        out["created_by_iam_user"] = data["CreatedByIamUser"]
    if "CreatedAt" in data:
        import aws_sdk_machine_learning.types.epoch_time

        out["created_at"] = (
            aws_sdk_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import aws_sdk_machine_learning.types.epoch_time

        out["last_updated_at"] = (
            aws_sdk_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["LastUpdatedAt"]
            )
        )
    if "DataSizeInBytes" in data:
        out["data_size_in_bytes"] = data["DataSizeInBytes"]
    if "NumberOfFiles" in data:
        out["number_of_files"] = data["NumberOfFiles"]
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_machine_learning.types.entity_status

        out["status"] = (
            aws_sdk_machine_learning.types.entity_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "LogUri" in data:
        out["log_uri"] = data["LogUri"]
    if "Message" in data:
        out["message"] = data["Message"]
    if "RedshiftMetadata" in data:
        import aws_sdk_machine_learning.types.redshift_metadata

        out["redshift_metadata"] = (
            aws_sdk_machine_learning.types.redshift_metadata.deserialize_aws_json_1_1(
                data["RedshiftMetadata"]
            )
        )
    if "RDSMetadata" in data:
        import aws_sdk_machine_learning.types.rds_metadata

        out["rds_metadata"] = (
            aws_sdk_machine_learning.types.rds_metadata.deserialize_aws_json_1_1(
                data["RDSMetadata"]
            )
        )
    if "RoleARN" in data:
        out["role_arn"] = data["RoleARN"]
    if "ComputeStatistics" in data:
        out["compute_statistics"] = data["ComputeStatistics"]
    else:
        out["compute_statistics"] = False
    if "ComputeTime" in data:
        out["compute_time"] = data["ComputeTime"]
    if "FinishedAt" in data:
        import aws_sdk_machine_learning.types.epoch_time

        out["finished_at"] = (
            aws_sdk_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["FinishedAt"]
            )
        )
    if "StartedAt" in data:
        import aws_sdk_machine_learning.types.epoch_time

        out["started_at"] = (
            aws_sdk_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["StartedAt"]
            )
        )
    if "DataSourceSchema" in data:
        out["data_source_schema"] = data["DataSourceSchema"]
    return out
