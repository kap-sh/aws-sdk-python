"""Generated from Smithy shape ``com.amazonaws.machinelearning#GetEvaluationOutput``."""

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
    import aws_sdk_machine_learning.types.presigned_s3_url
    import aws_sdk_machine_learning.types.s3_url


class GetEvaluationOutput(TypedDict):
    evaluation_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The evaluation ID which is same as the <code>EvaluationId</code> in the request.</p>"""
    ml_model_id: NotRequired["aws_sdk_machine_learning.types.entity_id.EntityId"]
    """<p>The ID of the <code>MLModel</code> that was the focus of the evaluation.</p>"""
    evaluation_data_source_id: NotRequired[
        "aws_sdk_machine_learning.types.entity_id.EntityId"
    ]
    """<p>The <code>DataSource</code> used for this evaluation.</p>"""
    input_data_location_s3: NotRequired["aws_sdk_machine_learning.types.s3_url.S3Url"]
    """<p>The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).</p>"""
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
    """<p>The status of the evaluation. This element can have one of the following values:</p> <ul> <li> <p> <code>PENDING</code> - Amazon Machine Language (Amazon ML) submitted a request to evaluate an <code>MLModel</code>.</p> </li> <li> <p> <code>INPROGRESS</code> - The evaluation is underway.</p> </li> <li> <p> <code>FAILED</code> - The request to evaluate an <code>MLModel</code> did not run to completion. It is not usable.</p> </li> <li> <p> <code>COMPLETED</code> - The evaluation process completed successfully.</p> </li> <li> <p> <code>DELETED</code> - The <code>Evaluation</code> is marked as deleted. It is not usable.</p> </li> </ul>"""
    performance_metrics: NotRequired[
        "aws_sdk_machine_learning.types.performance_metrics.PerformanceMetrics"
    ]
    """<p>Measurements of how well the <code>MLModel</code> performed using observations referenced by the <code>DataSource</code>. One of the following metric is returned based on the type of the <code>MLModel</code>: </p> <ul> <li> <p>BinaryAUC: A binary <code>MLModel</code> uses the Area Under the Curve (AUC) technique to measure performance. </p> </li> <li> <p>RegressionRMSE: A regression <code>MLModel</code> uses the Root Mean Square Error (RMSE) technique to measure performance. RMSE measures the difference between predicted and actual values for a single variable.</p> </li> <li> <p>MulticlassAvgFScore: A multiclass <code>MLModel</code> uses the F1 score technique to measure performance. </p> </li> </ul> <p> For more information about performance metrics, please see the <a href=\"https://docs.aws.amazon.com/machine-learning/latest/dg\">Amazon Machine Learning Developer Guide</a>. </p>"""
    log_uri: NotRequired[
        "aws_sdk_machine_learning.types.presigned_s3_url.PresignedS3Url"
    ]
    """<p>A link to the file that contains logs of the <code>CreateEvaluation</code> operation.</p>"""
    message: NotRequired["aws_sdk_machine_learning.types.message.Message"]
    """<p>A description of the most recent details about evaluating the <code>MLModel</code>.</p>"""
    compute_time: NotRequired["aws_sdk_machine_learning.types.long_type.LongType"]
    """<p>The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the <code>Evaluation</code>, normalized and scaled on computation resources. <code>ComputeTime</code> is only available if the <code>Evaluation</code> is in the <code>COMPLETED</code> state.</p>"""
    finished_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The epoch time when Amazon Machine Learning marked the <code>Evaluation</code> as <code>COMPLETED</code> or <code>FAILED</code>. <code>FinishedAt</code> is only available when the <code>Evaluation</code> is in the <code>COMPLETED</code> or <code>FAILED</code> state.</p>"""
    started_at: NotRequired["aws_sdk_machine_learning.types.epoch_time.EpochTime"]
    """<p>The epoch time when Amazon Machine Learning marked the <code>Evaluation</code> as <code>INPROGRESS</code>. <code>StartedAt</code> isn't available if the <code>Evaluation</code> is in the <code>PENDING</code> state.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEvaluationOutput) -> dict:
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
    if "log_uri" in value:
        out["LogUri"] = value["log_uri"]
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


def deserialize_aws_json_1_1(data: dict) -> GetEvaluationOutput:
    out: GetEvaluationOutput = {}  # type: ignore[typeddict-item]
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
    if "LogUri" in data:
        out["log_uri"] = data["LogUri"]
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
