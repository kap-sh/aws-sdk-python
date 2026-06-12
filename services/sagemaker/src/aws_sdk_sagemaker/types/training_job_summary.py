"""Generated from Smithy shape ``com.amazonaws.sagemaker#TrainingJobSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.secondary_status
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_job_arn
    import aws_sdk_sagemaker.types.training_job_name
    import aws_sdk_sagemaker.types.training_job_status
    import aws_sdk_sagemaker.types.training_plan_arn
    import aws_sdk_sagemaker.types.warm_pool_status


class TrainingJobSummary(TypedDict):
    training_job_name: NotRequired[
        "aws_sdk_sagemaker.types.training_job_name.TrainingJobName"
    ]
    """<p>The name of the training job that you want a summary for.</p>"""
    training_job_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_job_arn.TrainingJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the training job.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the training job was created.</p>"""
    training_end_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the training job ended. This field is set only if the training job has one of the terminal statuses (<code>Completed</code>, <code>Failed</code>, or <code>Stopped</code>). </p>"""
    last_modified_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p> Timestamp when the training job was last modified. </p>"""
    training_job_status: NotRequired[
        "aws_sdk_sagemaker.types.training_job_status.TrainingJobStatus"
    ]
    """<p>The status of the training job.</p>"""
    secondary_status: NotRequired[
        "aws_sdk_sagemaker.types.secondary_status.SecondaryStatus"
    ]
    """<p>The secondary status of the training job.</p>"""
    warm_pool_status: NotRequired[
        "aws_sdk_sagemaker.types.warm_pool_status.WarmPoolStatus"
    ]
    """<p>The status of the warm pool associated with the training job.</p>"""
    training_plan_arn: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arn.TrainingPlanArn"
    ]
    """<p>The Amazon Resource Name (ARN); of the training plan associated with this training job.</p> <p>For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html\">CreateTrainingPlan</a> </code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TrainingJobSummary) -> dict:
    out: dict = {}
    if "training_job_name" in value:
        out["TrainingJobName"] = value["training_job_name"]
    if "training_job_arn" in value:
        out["TrainingJobArn"] = value["training_job_arn"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "training_end_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["TrainingEndTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["training_end_time"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "training_job_status" in value:
        import aws_sdk_sagemaker.types.training_job_status

        out["TrainingJobStatus"] = (
            aws_sdk_sagemaker.types.training_job_status.serialize_aws_json_1_1(
                value["training_job_status"]
            )
        )
    if "secondary_status" in value:
        import aws_sdk_sagemaker.types.secondary_status

        out["SecondaryStatus"] = (
            aws_sdk_sagemaker.types.secondary_status.serialize_aws_json_1_1(
                value["secondary_status"]
            )
        )
    if "warm_pool_status" in value:
        import aws_sdk_sagemaker.types.warm_pool_status

        out["WarmPoolStatus"] = (
            aws_sdk_sagemaker.types.warm_pool_status.serialize_aws_json_1_1(
                value["warm_pool_status"]
            )
        )
    if "training_plan_arn" in value:
        out["TrainingPlanArn"] = value["training_plan_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TrainingJobSummary:
    out: TrainingJobSummary = {}  # type: ignore[typeddict-item]
    if "TrainingJobName" in data:
        out["training_job_name"] = data["TrainingJobName"]
    if "TrainingJobArn" in data:
        out["training_job_arn"] = data["TrainingJobArn"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "TrainingEndTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["training_end_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["TrainingEndTime"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "TrainingJobStatus" in data:
        import aws_sdk_sagemaker.types.training_job_status

        out["training_job_status"] = (
            aws_sdk_sagemaker.types.training_job_status.deserialize_aws_json_1_1(
                data["TrainingJobStatus"]
            )
        )
    if "SecondaryStatus" in data:
        import aws_sdk_sagemaker.types.secondary_status

        out["secondary_status"] = (
            aws_sdk_sagemaker.types.secondary_status.deserialize_aws_json_1_1(
                data["SecondaryStatus"]
            )
        )
    if "WarmPoolStatus" in data:
        import aws_sdk_sagemaker.types.warm_pool_status

        out["warm_pool_status"] = (
            aws_sdk_sagemaker.types.warm_pool_status.deserialize_aws_json_1_1(
                data["WarmPoolStatus"]
            )
        )
    if "TrainingPlanArn" in data:
        out["training_plan_arn"] = data["TrainingPlanArn"]
    return out
