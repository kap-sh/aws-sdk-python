"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateOptimizationJobRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.entity_name
    import aws_sdk_sagemaker.types.optimization_configs
    import aws_sdk_sagemaker.types.optimization_job_deployment_instance_type
    import aws_sdk_sagemaker.types.optimization_job_environment_variables
    import aws_sdk_sagemaker.types.optimization_job_max_instance_count
    import aws_sdk_sagemaker.types.optimization_job_model_source
    import aws_sdk_sagemaker.types.optimization_job_output_config
    import aws_sdk_sagemaker.types.optimization_vpc_config
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.stopping_condition
    import aws_sdk_sagemaker.types.tag_list


class CreateOptimizationJobRequest(TypedDict):
    optimization_job_name: NotRequired["aws_sdk_sagemaker.types.entity_name.EntityName"]
    """<p>A custom name for the new optimization job.</p>"""
    role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of an IAM role that enables Amazon SageMaker AI to perform tasks on your behalf. </p> <p>During model optimization, Amazon SageMaker AI needs your permission to:</p> <ul> <li> <p>Read input data from an S3 bucket</p> </li> <li> <p>Write model artifacts to an S3 bucket</p> </li> <li> <p>Write logs to Amazon CloudWatch Logs</p> </li> <li> <p>Publish metrics to Amazon CloudWatch</p> </li> </ul> <p>You grant permissions for all of these tasks to an IAM role. To pass this role to Amazon SageMaker AI, the caller of this API must have the <code>iam:PassRole</code> permission. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html\">Amazon SageMaker AI Roles.</a> </p>"""
    model_source: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_model_source.OptimizationJobModelSource"
    ]
    """<p>The location of the source model to optimize with an optimization job.</p>"""
    deployment_instance_type: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_deployment_instance_type.OptimizationJobDeploymentInstanceType"
    ]
    """<p>The type of instance that hosts the optimized model that you create with the optimization job.</p>"""
    max_instance_count: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_max_instance_count.OptimizationJobMaxInstanceCount"
    ]
    """<p>The maximum number of instances to use for the optimization job.</p>"""
    optimization_environment: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_environment_variables.OptimizationJobEnvironmentVariables"
    ]
    """<p>The environment variables to set in the model container.</p>"""
    optimization_configs: NotRequired[
        "aws_sdk_sagemaker.types.optimization_configs.OptimizationConfigs"
    ]
    """<p>Settings for each of the optimization techniques that the job applies.</p>"""
    output_config: NotRequired[
        "aws_sdk_sagemaker.types.optimization_job_output_config.OptimizationJobOutputConfig"
    ]
    """<p>Details for where to store the optimized model that you create with the optimization job.</p>"""
    stopping_condition: NotRequired[
        "aws_sdk_sagemaker.types.stopping_condition.StoppingCondition"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>A list of key-value pairs associated with the optimization job. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services resources</a> in the <i>Amazon Web Services General Reference Guide</i>.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_sagemaker.types.optimization_vpc_config.OptimizationVpcConfig"
    ]
    """<p>A VPC in Amazon VPC that your optimized model has access to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateOptimizationJobRequest) -> dict:
    out: dict = {}
    if "optimization_job_name" in value:
        out["OptimizationJobName"] = value["optimization_job_name"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "model_source" in value:
        import aws_sdk_sagemaker.types.optimization_job_model_source

        out["ModelSource"] = (
            aws_sdk_sagemaker.types.optimization_job_model_source.serialize_aws_json_1_1(
                value["model_source"]
            )
        )
    if "deployment_instance_type" in value:
        import aws_sdk_sagemaker.types.optimization_job_deployment_instance_type

        out["DeploymentInstanceType"] = (
            aws_sdk_sagemaker.types.optimization_job_deployment_instance_type.serialize_aws_json_1_1(
                value["deployment_instance_type"]
            )
        )
    if "max_instance_count" in value:
        out["MaxInstanceCount"] = value["max_instance_count"]
    if "optimization_environment" in value:
        import aws_sdk_sagemaker.types.optimization_job_environment_variables

        out["OptimizationEnvironment"] = (
            aws_sdk_sagemaker.types.optimization_job_environment_variables.serialize_aws_json_1_1(
                value["optimization_environment"]
            )
        )
    if "optimization_configs" in value:
        import aws_sdk_sagemaker.types.optimization_configs

        out["OptimizationConfigs"] = (
            aws_sdk_sagemaker.types.optimization_configs.serialize_aws_json_1_1(
                value["optimization_configs"]
            )
        )
    if "output_config" in value:
        import aws_sdk_sagemaker.types.optimization_job_output_config

        out["OutputConfig"] = (
            aws_sdk_sagemaker.types.optimization_job_output_config.serialize_aws_json_1_1(
                value["output_config"]
            )
        )
    if "stopping_condition" in value:
        import aws_sdk_sagemaker.types.stopping_condition

        out["StoppingCondition"] = (
            aws_sdk_sagemaker.types.stopping_condition.serialize_aws_json_1_1(
                value["stopping_condition"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_config" in value:
        import aws_sdk_sagemaker.types.optimization_vpc_config

        out["VpcConfig"] = (
            aws_sdk_sagemaker.types.optimization_vpc_config.serialize_aws_json_1_1(
                value["vpc_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateOptimizationJobRequest:
    out: CreateOptimizationJobRequest = {}  # type: ignore[typeddict-item]
    if "OptimizationJobName" in data:
        out["optimization_job_name"] = data["OptimizationJobName"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "ModelSource" in data:
        import aws_sdk_sagemaker.types.optimization_job_model_source

        out["model_source"] = (
            aws_sdk_sagemaker.types.optimization_job_model_source.deserialize_aws_json_1_1(
                data["ModelSource"]
            )
        )
    if "DeploymentInstanceType" in data:
        import aws_sdk_sagemaker.types.optimization_job_deployment_instance_type

        out["deployment_instance_type"] = (
            aws_sdk_sagemaker.types.optimization_job_deployment_instance_type.deserialize_aws_json_1_1(
                data["DeploymentInstanceType"]
            )
        )
    if "MaxInstanceCount" in data:
        out["max_instance_count"] = data["MaxInstanceCount"]
    if "OptimizationEnvironment" in data:
        import aws_sdk_sagemaker.types.optimization_job_environment_variables

        out["optimization_environment"] = (
            aws_sdk_sagemaker.types.optimization_job_environment_variables.deserialize_aws_json_1_1(
                data["OptimizationEnvironment"]
            )
        )
    if "OptimizationConfigs" in data:
        import aws_sdk_sagemaker.types.optimization_configs

        out["optimization_configs"] = (
            aws_sdk_sagemaker.types.optimization_configs.deserialize_aws_json_1_1(
                data["OptimizationConfigs"]
            )
        )
    if "OutputConfig" in data:
        import aws_sdk_sagemaker.types.optimization_job_output_config

        out["output_config"] = (
            aws_sdk_sagemaker.types.optimization_job_output_config.deserialize_aws_json_1_1(
                data["OutputConfig"]
            )
        )
    if "StoppingCondition" in data:
        import aws_sdk_sagemaker.types.stopping_condition

        out["stopping_condition"] = (
            aws_sdk_sagemaker.types.stopping_condition.deserialize_aws_json_1_1(
                data["StoppingCondition"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "VpcConfig" in data:
        import aws_sdk_sagemaker.types.optimization_vpc_config

        out["vpc_config"] = (
            aws_sdk_sagemaker.types.optimization_vpc_config.deserialize_aws_json_1_1(
                data["VpcConfig"]
            )
        )
    return out
