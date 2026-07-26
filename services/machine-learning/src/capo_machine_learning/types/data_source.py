"""Generated from Smithy shape ``com.amazonaws.machinelearning#DataSource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_machine_learning.types.aws_user_arn
    import capo_machine_learning.types.compute_statistics
    import capo_machine_learning.types.data_rearrangement
    import capo_machine_learning.types.entity_id
    import capo_machine_learning.types.entity_name
    import capo_machine_learning.types.entity_status
    import capo_machine_learning.types.epoch_time
    import capo_machine_learning.types.long_type
    import capo_machine_learning.types.message
    import capo_machine_learning.types.rds_metadata
    import capo_machine_learning.types.redshift_metadata
    import capo_machine_learning.types.role_arn
    import capo_machine_learning.types.s3_url


class DataSource(TypedDict, closed=True):
    data_source_id: NotRequired["capo_machine_learning.types.entity_id.EntityId"]
    """<p>The ID that is assigned to the <code>DataSource</code> during creation.</p>"""
    data_location_s3: NotRequired["capo_machine_learning.types.s3_url.S3Url"]
    """<p>The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is used by a <code>DataSource</code>.</p>"""
    data_rearrangement: NotRequired[
        "capo_machine_learning.types.data_rearrangement.DataRearrangement"
    ]
    """<p>A JSON string that represents the splitting and rearrangement requirement used when this <code>DataSource</code> was created.</p>"""
    created_by_iam_user: NotRequired[
        "capo_machine_learning.types.aws_user_arn.AwsUserArn"
    ]
    """<p>The AWS user account from which the <code>DataSource</code> was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.</p>"""
    created_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the <code>DataSource</code> was created. The time is expressed in epoch time.</p>"""
    last_updated_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time of the most recent edit to the <code>BatchPrediction</code>. The time is expressed in epoch time.</p>"""
    data_size_in_bytes: NotRequired["capo_machine_learning.types.long_type.LongType"]
    """<p>The total number of observations contained in the data files that the <code>DataSource</code> references.</p>"""
    number_of_files: NotRequired["capo_machine_learning.types.long_type.LongType"]
    """<p>The number of data files referenced by the <code>DataSource</code>.</p>"""
    name: NotRequired["capo_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>DataSource</code>.</p>"""
    status: NotRequired["capo_machine_learning.types.entity_status.EntityStatus"]
    """<p>The current status of the <code>DataSource</code>. This element can have one of the following values: </p> <ul> <li> <p>PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a <code>DataSource</code>.</p> </li> <li> <p>INPROGRESS - The creation process is underway.</p> </li> <li> <p>FAILED - The request to create a <code>DataSource</code> did not run to completion. It is not usable.</p> </li> <li> <p>COMPLETED - The creation process completed successfully.</p> </li> <li> <p>DELETED - The <code>DataSource</code> is marked as deleted. It is not usable.</p> </li> </ul>"""
    message: NotRequired["capo_machine_learning.types.message.Message"]
    """<p>A description of the most recent details about creating the <code>DataSource</code>.</p>"""
    redshift_metadata: NotRequired[
        "capo_machine_learning.types.redshift_metadata.RedshiftMetadata"
    ]
    rds_metadata: NotRequired["capo_machine_learning.types.rds_metadata.RDSMetadata"]
    role_arn: NotRequired["capo_machine_learning.types.role_arn.RoleARN"]
    compute_statistics: (
        "capo_machine_learning.types.compute_statistics.ComputeStatistics"
    )
    """<p> The parameter is <code>true</code> if statistics need to be generated from the observation data. </p>"""
    compute_time: NotRequired["capo_machine_learning.types.long_type.LongType"]
    finished_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]
    started_at: NotRequired["capo_machine_learning.types.epoch_time.EpochTime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DataSource) -> dict:
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
        import capo_machine_learning.types.epoch_time

        out["CreatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["created_at"]
            )
        )
    if "last_updated_at" in value:
        import capo_machine_learning.types.epoch_time

        out["LastUpdatedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
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
        import capo_machine_learning.types.entity_status

        out["Status"] = (
            capo_machine_learning.types.entity_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "message" in value:
        out["Message"] = value["message"]
    if "redshift_metadata" in value:
        import capo_machine_learning.types.redshift_metadata

        out["RedshiftMetadata"] = (
            capo_machine_learning.types.redshift_metadata.serialize_aws_json_1_1(
                value["redshift_metadata"]
            )
        )
    if "rds_metadata" in value:
        import capo_machine_learning.types.rds_metadata

        out["RDSMetadata"] = (
            capo_machine_learning.types.rds_metadata.serialize_aws_json_1_1(
                value["rds_metadata"]
            )
        )
    if "role_arn" in value:
        out["RoleARN"] = value["role_arn"]
    out["ComputeStatistics"] = value.get("compute_statistics", False)
    if "compute_time" in value:
        out["ComputeTime"] = value["compute_time"]
    if "finished_at" in value:
        import capo_machine_learning.types.epoch_time

        out["FinishedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["finished_at"]
            )
        )
    if "started_at" in value:
        import capo_machine_learning.types.epoch_time

        out["StartedAt"] = (
            capo_machine_learning.types.epoch_time.serialize_aws_json_1_1(
                value["started_at"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DataSource:
    out: DataSource = {}  # type: ignore[typeddict-item]
    if "DataSourceId" in data:
        out["data_source_id"] = data["DataSourceId"]
    if "DataLocationS3" in data:
        out["data_location_s3"] = data["DataLocationS3"]
    if "DataRearrangement" in data:
        out["data_rearrangement"] = data["DataRearrangement"]
    if "CreatedByIamUser" in data:
        out["created_by_iam_user"] = data["CreatedByIamUser"]
    if "CreatedAt" in data:
        import capo_machine_learning.types.epoch_time

        out["created_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["CreatedAt"]
            )
        )
    if "LastUpdatedAt" in data:
        import capo_machine_learning.types.epoch_time

        out["last_updated_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
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
        import capo_machine_learning.types.entity_status

        out["status"] = (
            capo_machine_learning.types.entity_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "Message" in data:
        out["message"] = data["Message"]
    if "RedshiftMetadata" in data:
        import capo_machine_learning.types.redshift_metadata

        out["redshift_metadata"] = (
            capo_machine_learning.types.redshift_metadata.deserialize_aws_json_1_1(
                data["RedshiftMetadata"]
            )
        )
    if "RDSMetadata" in data:
        import capo_machine_learning.types.rds_metadata

        out["rds_metadata"] = (
            capo_machine_learning.types.rds_metadata.deserialize_aws_json_1_1(
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
        import capo_machine_learning.types.epoch_time

        out["finished_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["FinishedAt"]
            )
        )
    if "StartedAt" in data:
        import capo_machine_learning.types.epoch_time

        out["started_at"] = (
            capo_machine_learning.types.epoch_time.deserialize_aws_json_1_1(
                data["StartedAt"]
            )
        )
    return out
