"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateModelInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.boolean
    import aws_sdk_sagemaker.types.container_definition
    import aws_sdk_sagemaker.types.container_definition_list
    import aws_sdk_sagemaker.types.inference_execution_config
    import aws_sdk_sagemaker.types.model_name
    import aws_sdk_sagemaker.types.role_arn
    import aws_sdk_sagemaker.types.tag_list
    import aws_sdk_sagemaker.types.vpc_config


class CreateModelInput(TypedDict, closed=True):
    model_name: NotRequired["aws_sdk_sagemaker.types.model_name.ModelName"]
    """<p>The name of the new model.</p>"""
    primary_container: NotRequired[
        "aws_sdk_sagemaker.types.container_definition.ContainerDefinition"
    ]
    """<p>The location of the primary docker image containing inference code, associated artifacts, and custom environment map that the inference code uses when the model is deployed for predictions. </p>"""
    containers: NotRequired[
        "aws_sdk_sagemaker.types.container_definition_list.ContainerDefinitionList"
    ]
    """<p>Specifies the containers in the inference pipeline.</p>"""
    inference_execution_config: NotRequired[
        "aws_sdk_sagemaker.types.inference_execution_config.InferenceExecutionConfig"
    ]
    """<p>Specifies details of how containers in a multi-container endpoint are called.</p>"""
    execution_role_arn: NotRequired["aws_sdk_sagemaker.types.role_arn.RoleArn"]
    r"""<p>The Amazon Resource Name (ARN) of the IAM role that SageMaker can assume to access model artifacts and docker image for deployment on ML compute instances or for batch transform jobs. Deploying on ML compute instances is part of model hosting. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html\">SageMaker Roles</a>. </p> <note> <p>To be able to pass this role to SageMaker, the caller of this API must have the <code>iam:PassRole</code> permission.</p> </note>"""
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p>"""
    vpc_config: NotRequired["aws_sdk_sagemaker.types.vpc_config.VpcConfig"]
    r"""<p>A <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_VpcConfig.html\">VpcConfig</a> object that specifies the VPC that you want your model to connect to. Control access to and from your model container by configuring the VPC. <code>VpcConfig</code> is used in hosting services and in batch transform. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/host-vpc.html\">Protect Endpoints by Using an Amazon Virtual Private Cloud</a> and <a href=\"https://docs.aws.amazon.com/sagemaker/latest/dg/batch-vpc.html\">Protect Data in Batch Transform Jobs by Using an Amazon Virtual Private Cloud</a>.</p>"""
    enable_network_isolation: NotRequired["aws_sdk_sagemaker.types.boolean.Boolean"]
    """<p>Isolates the model container. No inbound or outbound network calls can be made to or from the model container.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateModelInput) -> dict:
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
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "vpc_config" in value:
        import aws_sdk_sagemaker.types.vpc_config

        out["VpcConfig"] = aws_sdk_sagemaker.types.vpc_config.serialize_aws_json_1_1(
            value["vpc_config"]
        )
    if "enable_network_isolation" in value:
        out["EnableNetworkIsolation"] = value["enable_network_isolation"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateModelInput:
    out: CreateModelInput = {}  # type: ignore[typeddict-item]
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
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "VpcConfig" in data:
        import aws_sdk_sagemaker.types.vpc_config

        out["vpc_config"] = aws_sdk_sagemaker.types.vpc_config.deserialize_aws_json_1_1(
            data["VpcConfig"]
        )
    if "EnableNetworkIsolation" in data:
        out["enable_network_isolation"] = data["EnableNetworkIsolation"]
    return out
