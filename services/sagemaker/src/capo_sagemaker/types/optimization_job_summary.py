"""Generated from Smithy shape ``com.amazonaws.sagemaker#OptimizationJobSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.optimization_job_arn
    import capo_sagemaker.types.optimization_job_deployment_instance_type
    import capo_sagemaker.types.optimization_job_max_instance_count
    import capo_sagemaker.types.optimization_job_status
    import capo_sagemaker.types.optimization_types
    import capo_sagemaker.types.timestamp


class OptimizationJobSummary(TypedDict, closed=True):
    optimization_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name that you assigned to the optimization job.</p>"""
    optimization_job_arn: NotRequired[
        "capo_sagemaker.types.optimization_job_arn.OptimizationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the optimization job.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The time when you created the optimization job.</p>"""
    optimization_job_status: NotRequired[
        "capo_sagemaker.types.optimization_job_status.OptimizationJobStatus"
    ]
    """<p>The current status of the optimization job.</p>"""
    optimization_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the optimization job started.</p>"""
    optimization_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the optimization job finished processing.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The time when the optimization job was last updated.</p>"""
    deployment_instance_type: NotRequired[
        "capo_sagemaker.types.optimization_job_deployment_instance_type.OptimizationJobDeploymentInstanceType"
    ]
    """<p>The type of instance that hosts the optimized model that you create with the optimization job.</p>"""
    max_instance_count: NotRequired[
        "capo_sagemaker.types.optimization_job_max_instance_count.OptimizationJobMaxInstanceCount"
    ]
    """<p>The maximum number of instances to use for the optimization job.</p>"""
    optimization_types: NotRequired[
        "capo_sagemaker.types.optimization_types.OptimizationTypes"
    ]
    """<p>The optimization techniques that are applied by the optimization job.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OptimizationJobSummary) -> dict:
    out: dict = {}
    if "optimization_job_name" in value:
        out["OptimizationJobName"] = value["optimization_job_name"]
    if "optimization_job_arn" in value:
        out["OptimizationJobArn"] = value["optimization_job_arn"]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "optimization_job_status" in value:
        import capo_sagemaker.types.optimization_job_status

        out["OptimizationJobStatus"] = (
            capo_sagemaker.types.optimization_job_status.serialize_aws_json_1_1(
                value["optimization_job_status"]
            )
        )
    if "optimization_start_time" in value:
        import capo_sagemaker.types.timestamp

        out["OptimizationStartTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["optimization_start_time"]
            )
        )
    if "optimization_end_time" in value:
        import capo_sagemaker.types.timestamp

        out["OptimizationEndTime"] = (
            capo_sagemaker.types.timestamp.serialize_aws_json_1_1(
                value["optimization_end_time"]
            )
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "deployment_instance_type" in value:
        import capo_sagemaker.types.optimization_job_deployment_instance_type

        out["DeploymentInstanceType"] = (
            capo_sagemaker.types.optimization_job_deployment_instance_type.serialize_aws_json_1_1(
                value["deployment_instance_type"]
            )
        )
    if "max_instance_count" in value:
        out["MaxInstanceCount"] = value["max_instance_count"]
    if "optimization_types" in value:
        import capo_sagemaker.types.optimization_types

        out["OptimizationTypes"] = (
            capo_sagemaker.types.optimization_types.serialize_aws_json_1_1(
                value["optimization_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> OptimizationJobSummary:
    out: OptimizationJobSummary = {}  # type: ignore[typeddict-item]
    if "OptimizationJobName" in data:
        out["optimization_job_name"] = data["OptimizationJobName"]
    if "OptimizationJobArn" in data:
        out["optimization_job_arn"] = data["OptimizationJobArn"]
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "OptimizationJobStatus" in data:
        import capo_sagemaker.types.optimization_job_status

        out["optimization_job_status"] = (
            capo_sagemaker.types.optimization_job_status.deserialize_aws_json_1_1(
                data["OptimizationJobStatus"]
            )
        )
    if "OptimizationStartTime" in data:
        import capo_sagemaker.types.timestamp

        out["optimization_start_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["OptimizationStartTime"]
            )
        )
    if "OptimizationEndTime" in data:
        import capo_sagemaker.types.timestamp

        out["optimization_end_time"] = (
            capo_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["OptimizationEndTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "DeploymentInstanceType" in data:
        import capo_sagemaker.types.optimization_job_deployment_instance_type

        out["deployment_instance_type"] = (
            capo_sagemaker.types.optimization_job_deployment_instance_type.deserialize_aws_json_1_1(
                data["DeploymentInstanceType"]
            )
        )
    if "MaxInstanceCount" in data:
        out["max_instance_count"] = data["MaxInstanceCount"]
    if "OptimizationTypes" in data:
        import capo_sagemaker.types.optimization_types

        out["optimization_types"] = (
            capo_sagemaker.types.optimization_types.deserialize_aws_json_1_1(
                data["OptimizationTypes"]
            )
        )
    return out
