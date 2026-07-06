"""Generated from Smithy shape ``com.amazonaws.sagemaker#JupyterLabAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.app_lifecycle_management
    import aws_sdk_sagemaker.types.code_repositories
    import aws_sdk_sagemaker.types.custom_images
    import aws_sdk_sagemaker.types.emr_settings
    import aws_sdk_sagemaker.types.lifecycle_config_arns
    import aws_sdk_sagemaker.types.resource_spec
    import aws_sdk_sagemaker.types.studio_lifecycle_config_arn


class JupyterLabAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "aws_sdk_sagemaker.types.resource_spec.ResourceSpec"
    ]
    custom_images: NotRequired["aws_sdk_sagemaker.types.custom_images.CustomImages"]
    """<p>A list of custom SageMaker images that are configured to run as a JupyterLab app.</p>"""
    lifecycle_config_arns: NotRequired[
        "aws_sdk_sagemaker.types.lifecycle_config_arns.LifecycleConfigArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle configurations attached to the user profile or domain. To remove a lifecycle config, you must set <code>LifecycleConfigArns</code> to an empty list.</p>"""
    code_repositories: NotRequired[
        "aws_sdk_sagemaker.types.code_repositories.CodeRepositories"
    ]
    """<p>A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.</p>"""
    app_lifecycle_management: NotRequired[
        "aws_sdk_sagemaker.types.app_lifecycle_management.AppLifecycleManagement"
    ]
    """<p>Indicates whether idle shutdown is activated for JupyterLab applications.</p>"""
    emr_settings: NotRequired["aws_sdk_sagemaker.types.emr_settings.EmrSettings"]
    """<p>The configuration parameters that specify the IAM roles assumed by the execution role of SageMaker (assumable roles) and the cluster instances or job execution environments (execution roles or runtime roles) to manage and access resources required for running Amazon EMR clusters or Amazon EMR Serverless applications.</p>"""
    built_in_lifecycle_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
    ]
    """<p>The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JupyterLabAppSettings) -> dict:
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
    if "code_repositories" in value:
        import aws_sdk_sagemaker.types.code_repositories

        out["CodeRepositories"] = (
            aws_sdk_sagemaker.types.code_repositories.serialize_aws_json_1_1(
                value["code_repositories"]
            )
        )
    if "app_lifecycle_management" in value:
        import aws_sdk_sagemaker.types.app_lifecycle_management

        out["AppLifecycleManagement"] = (
            aws_sdk_sagemaker.types.app_lifecycle_management.serialize_aws_json_1_1(
                value["app_lifecycle_management"]
            )
        )
    if "emr_settings" in value:
        import aws_sdk_sagemaker.types.emr_settings

        out["EmrSettings"] = (
            aws_sdk_sagemaker.types.emr_settings.serialize_aws_json_1_1(
                value["emr_settings"]
            )
        )
    if "built_in_lifecycle_config_arn" in value:
        out["BuiltInLifecycleConfigArn"] = value["built_in_lifecycle_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JupyterLabAppSettings:
    out: JupyterLabAppSettings = {}  # type: ignore[typeddict-item]
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
    if "CodeRepositories" in data:
        import aws_sdk_sagemaker.types.code_repositories

        out["code_repositories"] = (
            aws_sdk_sagemaker.types.code_repositories.deserialize_aws_json_1_1(
                data["CodeRepositories"]
            )
        )
    if "AppLifecycleManagement" in data:
        import aws_sdk_sagemaker.types.app_lifecycle_management

        out["app_lifecycle_management"] = (
            aws_sdk_sagemaker.types.app_lifecycle_management.deserialize_aws_json_1_1(
                data["AppLifecycleManagement"]
            )
        )
    if "EmrSettings" in data:
        import aws_sdk_sagemaker.types.emr_settings

        out["emr_settings"] = (
            aws_sdk_sagemaker.types.emr_settings.deserialize_aws_json_1_1(
                data["EmrSettings"]
            )
        )
    if "BuiltInLifecycleConfigArn" in data:
        out["built_in_lifecycle_config_arn"] = data["BuiltInLifecycleConfigArn"]
    return out
