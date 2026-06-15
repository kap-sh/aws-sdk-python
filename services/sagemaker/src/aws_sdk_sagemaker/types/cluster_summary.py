"""Generated from Smithy shape ``com.amazonaws.sagemaker#ClusterSummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.cluster_arn
    import aws_sdk_sagemaker.types.cluster_name
    import aws_sdk_sagemaker.types.cluster_status
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.training_plan_arns


class ClusterSummary(TypedDict):
    cluster_arn: NotRequired["aws_sdk_sagemaker.types.cluster_arn.ClusterArn"]
    """<p>The Amazon Resource Name (ARN) of the SageMaker HyperPod cluster.</p>"""
    cluster_name: NotRequired["aws_sdk_sagemaker.types.cluster_name.ClusterName"]
    """<p>The name of the SageMaker HyperPod cluster.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the SageMaker HyperPod cluster is created.</p>"""
    cluster_status: NotRequired["aws_sdk_sagemaker.types.cluster_status.ClusterStatus"]
    """<p>The status of the SageMaker HyperPod cluster.</p>"""
    training_plan_arns: NotRequired[
        "aws_sdk_sagemaker.types.training_plan_arns.TrainingPlanArns"
    ]
    r"""<p>A list of Amazon Resource Names (ARNs) of the training plans associated with this cluster.</p> <p>For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see <code> <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html\">CreateTrainingPlan</a> </code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ClusterSummary) -> dict:
    out: dict = {}
    if "cluster_arn" in value:
        out["ClusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["ClusterName"] = value["cluster_name"]
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "cluster_status" in value:
        import aws_sdk_sagemaker.types.cluster_status

        out["ClusterStatus"] = (
            aws_sdk_sagemaker.types.cluster_status.serialize_aws_json_1_1(
                value["cluster_status"]
            )
        )
    if "training_plan_arns" in value:
        import aws_sdk_sagemaker.types.training_plan_arns

        out["TrainingPlanArns"] = (
            aws_sdk_sagemaker.types.training_plan_arns.serialize_aws_json_1_1(
                value["training_plan_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ClusterSummary:
    out: ClusterSummary = {}  # type: ignore[typeddict-item]
    if "ClusterArn" in data:
        out["cluster_arn"] = data["ClusterArn"]
    if "ClusterName" in data:
        out["cluster_name"] = data["ClusterName"]
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ClusterStatus" in data:
        import aws_sdk_sagemaker.types.cluster_status

        out["cluster_status"] = (
            aws_sdk_sagemaker.types.cluster_status.deserialize_aws_json_1_1(
                data["ClusterStatus"]
            )
        )
    if "TrainingPlanArns" in data:
        import aws_sdk_sagemaker.types.training_plan_arns

        out["training_plan_arns"] = (
            aws_sdk_sagemaker.types.training_plan_arns.deserialize_aws_json_1_1(
                data["TrainingPlanArns"]
            )
        )
    return out
