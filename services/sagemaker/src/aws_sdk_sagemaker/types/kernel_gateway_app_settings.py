"""Generated from Smithy shape ``com.amazonaws.sagemaker#KernelGatewayAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.custom_images
    import aws_sdk_sagemaker.types.lifecycle_config_arns
    import aws_sdk_sagemaker.types.resource_spec


class KernelGatewayAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "aws_sdk_sagemaker.types.resource_spec.ResourceSpec"
    ]
    """<p>The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the KernelGateway app.</p> <note> <p>The Amazon SageMaker AI Studio UI does not use the default instance type value set here. The default instance type set here is used when Apps are created using the CLI or CloudFormation and the instance type parameter value is not passed.</p> </note>"""
    custom_images: NotRequired["aws_sdk_sagemaker.types.custom_images.CustomImages"]
    """<p>A list of custom SageMaker AI images that are configured to run as a KernelGateway app.</p> <p>The maximum number of custom images are as follows.</p> <ul> <li> <p>On a domain level: 200</p> </li> <li> <p>On a space level: 5</p> </li> <li> <p>On a user profile level: 5</p> </li> </ul>"""
    lifecycle_config_arns: NotRequired[
        "aws_sdk_sagemaker.types.lifecycle_config_arns.LifecycleConfigArns"
    ]
    """<p> The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the the user profile or domain.</p> <note> <p>To remove a Lifecycle Config, you must set <code>LifecycleConfigArns</code> to an empty list.</p> </note>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KernelGatewayAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import aws_sdk_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            aws_sdk_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    if "custom_images" in value:
        import aws_sdk_sagemaker.types.custom_images

        out["CustomImages"] = (
            aws_sdk_sagemaker.types.custom_images.serialize_aws_json_1_1(
                value["custom_images"]
            )
        )
    if "lifecycle_config_arns" in value:
        import aws_sdk_sagemaker.types.lifecycle_config_arns

        out["LifecycleConfigArns"] = (
            aws_sdk_sagemaker.types.lifecycle_config_arns.serialize_aws_json_1_1(
                value["lifecycle_config_arns"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> KernelGatewayAppSettings:
    out: KernelGatewayAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import aws_sdk_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            aws_sdk_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    if "CustomImages" in data:
        import aws_sdk_sagemaker.types.custom_images

        out["custom_images"] = (
            aws_sdk_sagemaker.types.custom_images.deserialize_aws_json_1_1(
                data["CustomImages"]
            )
        )
    if "LifecycleConfigArns" in data:
        import aws_sdk_sagemaker.types.lifecycle_config_arns

        out["lifecycle_config_arns"] = (
            aws_sdk_sagemaker.types.lifecycle_config_arns.deserialize_aws_json_1_1(
                data["LifecycleConfigArns"]
            )
        )
    return out
