"""Generated from Smithy shape ``com.amazonaws.machinelearning#Evaluation``."""

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
    import aws_sdk_machine_learning.types.performance_metrics
    import aws_sdk_machine_learning.types.s3_url


class Evaluation(TypedDict):
    evaluation_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID that is assigned to the <code>Evaluation</code> at creation.</p>"""
    ml_model_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID of the <code>MLModel</code> that is the focus of the evaluation.</p>"""
    evaluation_data_source_id: NotRequired[
        "aws_sdk_machine_learning.types.entity_id.EntityId"
    ]
    """<p>The ID of the <code>DataSource</code> that is used to evaluate the <code>MLModel</code>.</p>"""
    input_data_location_s3: NotRequired["aws_sdk_machine_learning.types.s3_url.S3Url"]
    """<p>The location and name of the data in Amazon Simple Storage Server (Amazon S3) that is used in the evaluation.</p>"""
    created_by_iam_user: NotRequired[
        "aws_sdk_machine_learning.types.aws_user_arn.AwsUserArn"
    ]
    """<p>The AWS user account that invoked the evaluation. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.</p>"""
    created_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time that the <code>Evaluation</code> was created. The time is expressed in epoch time.</p>"""
    last_updated_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The time of the most recent edit to the <code>Evaluation</code>. The time is expressed in epoch time.</p>"""
    name: NotRequired["aws_sdk_machine_learning.types.entity_name.EntityName"]
    """<p>A user-supplied name or description of the <code>Evaluation</code>. </p>"""
    status: NotRequired["aws_sdk_machine_learning.types.entity_status.EntityStatus"]
    """<p>The status of the evaluation. This element can have one of the following values:</p> <ul> <li> <p> <code>PENDING</code> - Amazon Machine Learning (Amazon ML) submitted a request to evaluate an <code>MLModel</code>.</p> </li> <li> <p> <code>INPROGRESS</code> - The evaluation is underway.</p> </li> <li> <p> <code>FAILED</code> - The request to evaluate an <code>MLModel</code> did not run to completion. It is not usable.</p> </li> <li> <p> <code>COMPLETED</code> - The evaluation process completed successfully.</p> </li> <li> <p> <code>DELETED</code> - The <code>Evaluation</code> is marked as deleted. It is not usable.</p> </li> </ul>"""
    performance_metrics: NotRequired[
        "aws_sdk_machine_learning.types.performance_metrics.PerformanceMetrics"
    ]
    r"""<p>Measurements of how well the <code>MLModel</code> performed, using observations referenced by the <code>DataSource</code>. One of the following metrics is returned, based on the type of the <code>MLModel</code>: </p> <ul> <li> <p>BinaryAUC: A binary <code>MLModel</code> uses the Area Under the Curve (AUC) technique to measure performance. </p> </li> <li> <p>RegressionRMSE: A regression <code>MLModel</code> uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.</p> </li> <li> <p>MulticlassAvgFScore: A multiclass <code>MLModel</code> uses the F1 score technique to measure performance. </p> </li> </ul> <p> For more information about performance metrics, please see the <a href=\"https://docs.aws.amazon.com/machine-learning/latest/dg\">Amazon Machine Learning Developer Guide</a>. </p>"""
    message: NotRequired["aws_sdk_machine_learning.types.message.Message"]
    """<p>A description of the most recent details about evaluating the <code>MLModel</code>.</p>"""
    compute_time: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    finished_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    started_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Evaluation) -> dict:
    out: dict = {}
    if "evaluation_id" in value:
        out["EvaluationId"] = value["evaluation_id"]
    if "ml_model_id" in value:
        out["MLModelId"] = value["ml_model_id"]
    if "evaluation_data_source_id" in value:
        out["EvaluationDataSourceId"] = value["evaluation_data_source_id"]
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
    if "performance_metrics" in value:
        import aws_sdk_machine_learning.types.performance_metrics

        out["PerformanceMetrics"] = (
            aws_sdk_machine_learning.types.performance_metrics.serialize_aws_json_1_1(
                value["performance_metrics"]
            )
        )
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
    return out


def deserialize_aws_json_1_1(data: dict) -> Evaluation:
    out: Evaluation = {}  # type: ignore[typeddict-item]
    if "EvaluationId" in data:
        out["evaluation_id"] = data["EvaluationId"]
    if "MLModelId" in data:
        out["ml_model_id"] = data["MLModelId"]
    if "EvaluationDataSourceId" in data:
        out["evaluation_data_source_id"] = data["EvaluationDataSourceId"]
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
    if "PerformanceMetrics" in data:
        import aws_sdk_machine_learning.types.performance_metrics

        out["performance_metrics"] = (
            aws_sdk_machine_learning.types.performance_metrics.deserialize_aws_json_1_1(
                data["PerformanceMetrics"]
            )
        )
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
    return out
