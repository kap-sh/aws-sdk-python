"""Generated from Smithy shape ``com.amazonaws.sagemaker#CodeEditorAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.app_lifecycle_management
    import capo_sagemaker.types.custom_images
    import capo_sagemaker.types.lifecycle_config_arns
    import capo_sagemaker.types.resource_spec
    import capo_sagemaker.types.studio_lifecycle_config_arn


class CodeEditorAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "capo_sagemaker.types.resource_spec.ResourceSpec"
    ]
    custom_images: NotRequired["capo_sagemaker.types.custom_images.CustomImages"]
    """<p>A list of custom SageMaker images that are configured to run as a Code Editor app.</p>"""
    lifecycle_config_arns: NotRequired[
        "capo_sagemaker.types.lifecycle_config_arns.LifecycleConfigArns"
    ]
    """<p>The Amazon Resource Name (ARN) of the Code Editor application lifecycle configuration.</p>"""
    app_lifecycle_management: NotRequired[
        "capo_sagemaker.types.app_lifecycle_management.AppLifecycleManagement"
    ]
    """<p>Settings that are used to configure and manage the lifecycle of CodeEditor applications.</p>"""
    built_in_lifecycle_config_arn: NotRequired[
        "capo_sagemaker.types.studio_lifecycle_config_arn.StudioLifecycleConfigArn"
    ]
    """<p>The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CodeEditorAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    if "custom_images" in value:
        import capo_sagemaker.types.custom_images

        out["CustomImages"] = capo_sagemaker.types.custom_images.serialize_aws_json_1_1(
            value["custom_images"]
        )
    if "lifecycle_config_arns" in value:
        import capo_sagemaker.types.lifecycle_config_arns

        out["LifecycleConfigArns"] = (
            capo_sagemaker.types.lifecycle_config_arns.serialize_aws_json_1_1(
                value["lifecycle_config_arns"]
            )
        )
    if "app_lifecycle_management" in value:
        import capo_sagemaker.types.app_lifecycle_management

        out["AppLifecycleManagement"] = (
            capo_sagemaker.types.app_lifecycle_management.serialize_aws_json_1_1(
                value["app_lifecycle_management"]
            )
        )
    if "built_in_lifecycle_config_arn" in value:
        out["BuiltInLifecycleConfigArn"] = value["built_in_lifecycle_config_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CodeEditorAppSettings:
    out: CodeEditorAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import capo_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    if "CustomImages" in data:
        import capo_sagemaker.types.custom_images

        out["custom_images"] = (
            capo_sagemaker.types.custom_images.deserialize_aws_json_1_1(
                data["CustomImages"]
            )
        )
    if "LifecycleConfigArns" in data:
        import capo_sagemaker.types.lifecycle_config_arns

        out["lifecycle_config_arns"] = (
            capo_sagemaker.types.lifecycle_config_arns.deserialize_aws_json_1_1(
                data["LifecycleConfigArns"]
            )
        )
    if "AppLifecycleManagement" in data:
        import capo_sagemaker.types.app_lifecycle_management

        out["app_lifecycle_management"] = (
            capo_sagemaker.types.app_lifecycle_management.deserialize_aws_json_1_1(
                data["AppLifecycleManagement"]
            )
        )
    if "BuiltInLifecycleConfigArn" in data:
        out["built_in_lifecycle_config_arn"] = data["BuiltInLifecycleConfigArn"]
    return out
