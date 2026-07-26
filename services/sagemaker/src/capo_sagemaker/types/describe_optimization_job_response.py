"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeOptimizationJobResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.entity_name
    import capo_sagemaker.types.failure_reason
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.optimization_configs
    import capo_sagemaker.types.optimization_job_arn
    import capo_sagemaker.types.optimization_job_deployment_instance_type
    import capo_sagemaker.types.optimization_job_environment_variables
    import capo_sagemaker.types.optimization_job_max_instance_count
    import capo_sagemaker.types.optimization_job_model_source
    import capo_sagemaker.types.optimization_job_output_config
    import capo_sagemaker.types.optimization_job_status
    import capo_sagemaker.types.optimization_output
    import capo_sagemaker.types.optimization_vpc_config
    import capo_sagemaker.types.role_arn
    import capo_sagemaker.types.stopping_condition
    import capo_sagemaker.types.timestamp


class DescribeOptimizationJobResponse(TypedDict, closed=True):
    optimization_job_arn: NotRequired[
        "capo_sagemaker.types.optimization_job_arn.OptimizationJobArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the optimization job.</p>"""
    optimization_job_status: NotRequired[
        "capo_sagemaker.types.optimization_job_status.OptimizationJobStatus"
    ]
    """<p>The current status of the optimization job.</p>"""
    optimization_start_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the optimization job started.</p>"""
    optimization_end_time: NotRequired["capo_sagemaker.types.timestamp.Timestamp"]
    """<p>The time when the optimization job finished processing.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>The time when you created the optimization job.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>The time when the optimization job was last updated.</p>"""
    failure_reason: NotRequired["capo_sagemaker.types.failure_reason.FailureReason"]
    """<p>If the optimization job status is <code>FAILED</code>, the reason for the failure.</p>"""
    optimization_job_name: NotRequired["capo_sagemaker.types.entity_name.EntityName"]
    """<p>The name that you assigned to the optimization job.</p>"""
    model_source: NotRequired[
        "capo_sagemaker.types.optimization_job_model_source.OptimizationJobModelSource"
    ]
    """<p>The location of the source model to optimize with an optimization job.</p>"""
    optimization_environment: NotRequired[
        "capo_sagemaker.types.optimization_job_environment_variables.OptimizationJobEnvironmentVariables"
    ]
    """<p>The environment variables to set in the model container.</p>"""
    deployment_instance_type: NotRequired[
        "capo_sagemaker.types.optimization_job_deployment_instance_type.OptimizationJobDeploymentInstanceType"
    ]
    """<p>The type of instance that hosts the optimized model that you create with the optimization job.</p>"""
    max_instance_count: NotRequired[
        "capo_sagemaker.types.optimization_job_max_instance_count.OptimizationJobMaxInstanceCount"
    ]
    """<p>The maximum number of instances to use for the optimization job.</p>"""
    optimization_configs: NotRequired[
        "capo_sagemaker.types.optimization_configs.OptimizationConfigs"
    ]
    """<p>Settings for each of the optimization techniques that the job applies.</p>"""
    output_config: NotRequired[
        "capo_sagemaker.types.optimization_job_output_config.OptimizationJobOutputConfig"
    ]
    """<p>Details for where to store the optimized model that you create with the optimization job.</p>"""
    optimization_output: NotRequired[
        "capo_sagemaker.types.optimization_output.OptimizationOutput"
    ]
    """<p>Output values produced by an optimization job.</p>"""
    role_arn: NotRequired["capo_sagemaker.types.role_arn.RoleArn"]
    """<p>The ARN of the IAM role that you assigned to the optimization job.</p>"""
    stopping_condition: NotRequired[
        "capo_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    vpc_config: NotRequired[
        "capo_sagemaker.types.optimization_vpc_config.OptimizationVpcConfig"
    ]
    """<p>A VPC in Amazon VPC that your optimized model has access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeOptimizationJobResponse) -> dict:
    out: dict = {}
    if "optimization_job_arn" in value:
        out["OptimizationJobArn"] = value["optimization_job_arn"]
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
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    if "optimization_job_name" in value:
        out["OptimizationJobName"] = value["optimization_job_name"]
    if "model_source" in value:
        import capo_sagemaker.types.optimization_job_model_source

        out["ModelSource"] = (
            capo_sagemaker.types.optimization_job_model_source.serialize_aws_json_1_1(
                value["model_source"]
            )
        )
    if "optimization_environment" in value:
        import capo_sagemaker.types.optimization_job_environment_variables

        out["OptimizationEnvironment"] = (
            capo_sagemaker.types.optimization_job_environment_variables.serialize_aws_json_1_1(
                value["optimization_environment"]
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
    if "optimization_configs" in value:
        import capo_sagemaker.types.optimization_configs

        out["OptimizationConfigs"] = (
            capo_sagemaker.types.optimization_configs.serialize_aws_json_1_1(
                value["optimization_configs"]
            )
        )
    if "output_config" in value:
        import capo_sagemaker.types.optimization_job_output_config

        out["OutputConfig"] = (
            capo_sagemaker.types.optimization_job_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "optimization_output" in value:
        import capo_sagemaker.types.optimization_output

        out["OptimizationOutput"] = (
            capo_sagemaker.types.optimization_output.serialize_aws_json_1_1(
                value["optimization_output"]
            )
        )
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "stopping_condition" in value:
        import capo_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            capo_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "vpc_config" in value:
        import capo_sagemaker.types.optimization_vpc_config

        out["VpcConfig"] = (
            capo_sagemaker.types.optimization_vpc_config.serialize_aws_json_1_1(
                value["vpc_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeOptimizationJobResponse:
    out: DescribeOptimizationJobResponse = {}  # type: ignore[typeddict-item]
    if "OptimizationJobArn" in data:
        out["optimization_job_arn"] = data["OptimizationJobArn"]
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
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "FailureReason" in data:
        out["failure_reason"] = data["FailureReason"]
    if "OptimizationJobName" in data:
        out["optimization_job_name"] = data["OptimizationJobName"]
    if "ModelSource" in data:
        import capo_sagemaker.types.optimization_job_model_source

        out["model_source"] = (
            capo_sagemaker.types.optimization_job_model_source.deserialize_aws_json_1_1(
                data["ModelSource"]
            )
        )
    if "OptimizationEnvironment" in data:
        import capo_sagemaker.types.optimization_job_environment_variables

        out["optimization_environment"] = (
            capo_sagemaker.types.optimization_job_environment_variables.deserialize_aws_json_1_1(
                data["OptimizationEnvironment"]
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
    if "OptimizationConfigs" in data:
        import capo_sagemaker.types.optimization_configs

        out["optimization_configs"] = (
            capo_sagemaker.types.optimization_configs.deserialize_aws_json_1_1(
                data["OptimizationConfigs"]
            )
        )
    if "OutputConfig" in data:
        import capo_sagemaker.types.optimization_job_output_config

        out["output_config"] = (
            capo_sagemaker.types.optimization_job_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "OptimizationOutput" in data:
        import capo_sagemaker.types.optimization_output

        out["optimization_output"] = (
            capo_sagemaker.types.optimization_output.deserialize_aws_json_1_1(
                data["OptimizationOutput"]
            )
        )
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "StoppingCondition" in data:
        import capo_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            capo_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "VpcConfig" in data:
        import capo_sagemaker.types.optimization_vpc_config

        out["vpc_config"] = (
            capo_sagemaker.types.optimization_vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    return out
