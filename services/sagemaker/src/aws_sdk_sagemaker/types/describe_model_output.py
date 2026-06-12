"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeModelOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.container_definition
    import aws_sdk_sagemaker.types.container_definition_list
    import aws_sdk_sagemaker.types.deployment_recommendation
    import aws_sdk_sagemaker.types.inference_execution_config
    import aws_sdk_sagemaker.types.model_arn
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.timestamp
    import aws_sdk_sagemaker.types.vpc_config


class DescribeModelOutput(TypedDict):
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>Name of the SageMaker model.</p>"""
    primary_container: NotRequired[
        "aws_sdk_sagemaker.types.container_definition.ContainerDefinition"
    ]
    """<p>The location of the primary inference code, associated artifacts, and custom environment map that the inference code uses when it is deployed in production. </p>"""
    containers: NotRequired[
        "aws_sdk_sagemaker.types.container_definition_list.ContainerDefinitionList"
    ]
    """<p>The containers in the inference pipeline.</p>"""
    inference_execution_config: NotRequired[
        "aws_sdk_sagemaker.types.inference_execution_config.InferenceExecutionConfig"
    ]
    """<p>Specifies details of how containers in a multi-container endpoint are called.</p>"""
    execution_role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    """<p>The Amazon Resource Name (ARN) of the IAM role that you specified for the model.</p>"""
    vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    """<p>A <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html\">VpcConfig</a> object that specifies the VPC that this model has access to. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html\">Protect Endpoints by Using an Amazon Virtual Private Cloud</a> </p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.timestamp.Timestamp"]
    """<p>A timestamp that shows when the model was created.</p>"""
    model_arn: NotRequired["aws_sdk_sagemaker.types.model_arn.ModelArn"]
    """<p>The Amazon Resource Name (ARN) of the model.</p>"""
    enable_network_isolation: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>If <code>True</code>, no inbound or outbound network calls can be made to or from the model container.</p>"""
    deployment_recommendation: NotRequired[
        "aws_sdk_sagemaker.types.deployment_recommendation.DeploymentRecommendation"
    ]
    """<p>A set of recommended deployment configurations for the model.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeModelOutput) -> dict:
    out: dict = {}
    if "model_name" in value:
        out["ModelName"] = value["model_name"]
    if "primary_container" in value:
        import aws_sdk_sagemaker.types.container_definition

        out["PrimaryContainer"] = (
            aws_sdk_sagemaker.types.container_definition.serialize_aws_json_1_1(
                value["primary_container"]
            )
        )
    if "containers" in value:
        import aws_sdk_sagemaker.types.container_definition_list

        out["Containers"] = (
            aws_sdk_sagemaker.types.container_definition_list.serialize_aws_json_1_1(
                value["containers"]
            )
        )
    if "inference_execution_config" in value:
        import aws_sdk_sagemaker.types.inference_execution_config

        out["InferenceExecutionConfig"] = (
            aws_sdk_sagemaker.types.inference_execution_config.serialize_aws_json_1_1(
                value["inference_execution_config"]
            )
        )
    if "execution_role_arn" in value:
        out["ExecutionRoleArn"] = value["execution_role_arn"]
    if "vpc_config" in value:
        import aws_sdk_sagemaker.types.vpc_config

        out["VpcConfig"] = aws_sdk_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.timestamp

        out["CreationTime"] = aws_sdk_sagemaker.types.timestamp.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "model_arn" in value:
        out["ModelArn"] = value["model_arn"]
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    if "deployment_recommendation" in value:
        import aws_sdk_sagemaker.types.deployment_recommendation

        out["DeploymentRecommendation"] = (
            aws_sdk_sagemaker.types.deployment_recommendation.serialize_aws_json_1_1(
                value["deployment_recommendation"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeModelOutput:
    out: DescribeModelOutput = {}  # type: ignore[typeddict-item]
    if "ModelName" in data:
        out["model_name"] = data["ModelName"]
    if "PrimaryContainer" in data:
        import aws_sdk_sagemaker.types.container_definition

        out["primary_container"] = (
            aws_sdk_sagemaker.types.container_definition.deserialize_aws_json_1_1(
                data["PrimaryContainer"]
            )
        )
    if "Containers" in data:
        import aws_sdk_sagemaker.types.container_definition_list

        out["containers"] = (
            aws_sdk_sagemaker.types.container_definition_list.deserialize_aws_json_1_1(
                data["Containers"]
            )
        )
    if "InferenceExecutionConfig" in data:
        import aws_sdk_sagemaker.types.inference_execution_config

        out["inference_execution_config"] = (
            aws_sdk_sagemaker.types.inference_execution_config.deserialize_aws_json_1_1(
                data["InferenceExecutionConfig"]
            )
        )
    if "ExecutionRoleArn" in data:
        out["execution_role_arn"] = data["ExecutionRoleArn"]
    if "VpcConfig" in data:
        import aws_sdk_sagemaker.types.vpc_config

        out["vpc_config"] = aws_sdk_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.timestamp

        out["creation_time"] = (
            aws_sdk_sagemaker.types.timestamp.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "ModelArn" in data:
        out["model_arn"] = data["ModelArn"]
    if "EnableNetworkIsolation" in data:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    if "DeploymentRecommendation" in data:
        import aws_sdk_sagemaker.types.deployment_recommendation

        out["deployment_recommendation"] = (
            aws_sdk_sagemaker.types.deployment_recommendation.deserialize_aws_json_1_1(
                data["DeploymentRecommendation"]
            )
        )
    return out
