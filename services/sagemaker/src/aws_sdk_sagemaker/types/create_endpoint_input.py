"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateEndpointInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.deployment_config
    import aws_sdk_sagemaker.types.endpoint_config_name
    import aws_sdk_sagemaker.types.endpoint_name
    import aws_sdk_sagemaker.types.tag_list


class CreateEndpointInput(TypedDict):
    endpoint_name: NotRequired["aws_sdk_sagemaker.types.endpoint_name.EndpointName"]
    r"""<p>The name of the endpoint.The name must be unique within an Amazon Web Services Region in your Amazon Web Services account. The name is case-insensitive in <code>CreateEndpoint</code>, but the case is preserved and must be matched in <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_runtime_InvokeEndpoint.html\">InvokeEndpoint</a>.</p>"""
    endpoint_config_name: NotRequired[
        "aws_sdk_sagemaker.types.endpoint_config_name.EndpointConfigName"
    ]
    r"""<p>The name of an endpoint configuration. For more information, see <a href=\"https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateEndpointConfig.html\">CreateEndpointConfig</a>. </p>"""
    deployment_config: NotRequired[
        "aws_sdk_sagemaker.types.deployment_config.DeploymentConfig"
    ]
    tags: NotRequired["aws_sdk_sagemaker.types.tag_list.TagList"]
    r"""<p>An array of key-value pairs. You can use tags to categorize your Amazon Web Services resources in different ways, for example, by purpose, owner, or environment. For more information, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html\">Tagging Amazon Web Services Resources</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateEndpointInput) -> dict:
    out: dict = {}
    if "endpoint_name" in value:
        out["EndpointName"] = value["endpoint_name"]
    if "endpoint_config_name" in value:
        out["EndpointConfigName"] = value["endpoint_config_name"]
    if "deployment_config" in value:
        import aws_sdk_sagemaker.types.deployment_config

        out["DeploymentConfig"] = (
            aws_sdk_sagemaker.types.deployment_config.serialize_aws_json_1_1(
                value["deployment_config"]
            )
        )
    if "tags" in value:
        import aws_sdk_sagemaker.types.tag_list

        out["Tags"] = aws_sdk_sagemaker.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateEndpointInput:
    out: CreateEndpointInput = {}  # type: ignore[typeddict-item]
    if "EndpointName" in data:
        out["endpoint_name"] = data["EndpointName"]
    if "EndpointConfigName" in data:
        out["endpoint_config_name"] = data["EndpointConfigName"]
    if "DeploymentConfig" in data:
        import aws_sdk_sagemaker.types.deployment_config

        out["deployment_config"] = (
            aws_sdk_sagemaker.types.deployment_config.deserialize_aws_json_1_1(
                data["DeploymentConfig"]
            )
        )
    if "Tags" in data:
        import aws_sdk_sagemaker.types.tag_list

        out["tags"] = aws_sdk_sagemaker.types.tag_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    return out
