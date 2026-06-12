"""Generated from Smithy shape ``com.amazonaws.machinelearning#BatchPrediction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_machine_learning.types.aws_user_arn
    import aws_sdk_machine_learning.types.entity_id
    import aws_sdk_machine_learning.types.entity_name
    import aws_sdk_machine_learning.types.entity_status
    import aws_sdk_machine_learning.types.epoch_time
    import aws_sdk_machine_learning.types.long_type
    import aws_sdk_machine_learning.types.message
    import aws_sdk_machine_learning.types.s3_url


class BatchPrediction(TypedDict):
    batch_prediction_id: NotRequired[
        "aws_sdk_machine_learning.types.entity_id.EntityId"
    ]
    """<p>The ID assigned to the <code>BatchPrediction</code> at creation. This value should be identical to the value of the <code>BatchPredictionID</code> in the request. </p>"""
    ml_model_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID of the <code>MLModel</code> that generated predictions for the <code>BatchPrediction</code> request.</p>"""
    batch_prediction_data_source_id: NotRequired[
        "aws_sdk_machine_learning.types.entity_id.EntityId"
    ]
    """<p>The ID of the <code>DataSource</code> that points to the group of observations to predict.</p>"""
    input_data_location_s3: NotRequired["aws_sdk_machine_learning.types.s3_url.S3Url"]
    """<p>The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).</p>"""
    created_by_iam_user: NotRequired[
        "aws_sdk_machine_learning.types.aws_user_arn.AwsUserArn"
    ]
    """<p>The AWS user account that invoked the <code>BatchPrediction</code>. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.</p>"""
    created_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the <code>BatchPrediction</code> was created. The time is expressed in epoch time.</p>"""
    last_updated_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time of the most recent edit to the <code>BatchPrediction</code>. The time is expressed in epoch time.</p>"""
    name: NotRequired["aws_sdk_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>BatchPrediction</code>.</p>"""
    status: NotRequired["aws_sdk_machine_learning.types.entity_status.EntityStatus"]
    """<p>The status of the <code>BatchPrediction</code>. This element can have one of the following values:</p> <ul> <li> <p> <code>PENDING</code> - Amazon Machine Learning (Amazon ML) submitted a request to generate predictions for a batch of observations.</p> </li> <li> <p> <code>INPROGRESS</code> - The process is underway.</p> </li> <li> <p> <code>FAILED</code> - The request to perform a batch prediction did not run to completion. It is not usable.</p> </li> <li> <p> <code>COMPLETED</code> - The batch prediction process completed successfully.</p> </li> <li> <p> <code>DELETED</code> - The <code>BatchPrediction</code> is marked as deleted. It is not usable.</p> </li> </ul>"""
    output_uri: NotRequired["aws_sdk_machine_learning.types.s3_url.S3Url"]
    """<p>The location of an Amazon S3 bucket or directory to receive the operation results. The following substrings are not allowed in the <code>s3 key</code> portion of the <code>outputURI</code> field: ':', '//', '/./', '/../'.</p>"""
    message: NotRequired["aws_sdk_machine_learning.types.message.Message"]
    """<p>A description of the most recent details about processing the batch prediction request.</p>"""
    compute_time: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    finished_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    started_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    total_record_count: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    invalid_record_count: NotRequired[
        "aws_sdk_machine_learning.types.long_type.LongType"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchPrediction) -> dict:
    out: dict = {}
    if "batch_prediction_id" in value:
        out["BatchPredictionId"] = value["batch_prediction_id"]
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    if "batch_prediction_data_source_id" in value:
        out["BatchPredictionDataSourceId"] = value["batch_prediction_data_source_id"]
    if "input_data_location_s3" in value:
        out["InputDataLocationS3"] = value["input_data_location_s3"]
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
    if "name" in value:
        out["Name"] = value["name"]
    if "status" in value:
        import aws_sdk_machine_learning.types.entity_status

        out["Status"] = (
            aws_sdk_machine_learning.types.entity_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "output_uri" in value:
        out["OutputUri"] = value["output_uri"]
    if "message" in value:
        out["Message"] = value["message"]
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
    if "total_record_count" in value:
        out["TotalRecordCount"] = value["total_record_count"]
    if "invalid_record_count" in value:
        out["InvalidRecordCount"] = value["invalid_record_count"]
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchPrediction:
    out: BatchPrediction = {}  # type: ignore[typeddict-item]
    if "BatchPredictionId" in data:
        out["batch_prediction_id"] = data["BatchPredictionId"]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    if "BatchPredictionDataSourceId" in data:
        out["batch_prediction_data_source_id"] = data["BatchPredictionDataSourceId"]
    if "InputDataLocationS3" in data:
        out["input_data_location_s3"] = data["InputDataLocationS3"]
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
    if "Name" in data:
        out["name"] = data["Name"]
    if "Status" in data:
        import aws_sdk_machine_learning.types.entity_status

        out["status"] = (
            aws_sdk_machine_learning.types.entity_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "OutputUri" in data:
        out["output_uri"] = data["OutputUri"]
    if "Message" in data:
        out["message"] = data["Message"]
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
    if "TotalRecordCount" in data:
        out["total_record_count"] = data["TotalRecordCount"]
    if "InvalidRecordCount" in data:
        out["invalid_record_count"] = data["InvalidRecordCount"]
    return out
