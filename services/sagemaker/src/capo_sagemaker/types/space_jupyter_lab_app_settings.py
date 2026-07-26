"""Generated from Smithy shape ``com.amazonaws.sagemaker#SpaceJupyterLabAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.code_repositories
    import capo_sagemaker.types.resource_spec
    import capo_sagemaker.types.space_app_lifecycle_management


class SpaceJupyterLabAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "capo_sagemaker.types.resource_spec.ResourceSpec"
    ]
    code_repositories: NotRequired[
        "capo_sagemaker.types.code_repositories.CodeRepositories"
    ]
    """<p>A list of Git repositories that SageMaker automatically displays to users for cloning in the JupyterLab application.</p>"""
    app_lifecycle_management: NotRequired[
        "capo_sagemaker.types.space_app_lifecycle_management.SpaceAppLifecycleManagement"
    ]
    """<p>Settings that are used to configure and manage the lifecycle of JupyterLab applications in a space.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SpaceJupyterLabAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    if "code_repositories" in value:
        import capo_sagemaker.types.code_repositories

        out["CodeRepositories"] = (
            capo_sagemaker.types.code_repositories.serialize_aws_json_1_1(
                value["code_repositories"]
            )
        )
    if "app_lifecycle_management" in value:
        import capo_sagemaker.types.space_app_lifecycle_management

        out["AppLifecycleManagement"] = (
            capo_sagemaker.types.space_app_lifecycle_management.serialize_aws_json_1_1(
                value["app_lifecycle_management"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SpaceJupyterLabAppSettings:
    out: SpaceJupyterLabAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import capo_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    if "CodeRepositories" in data:
        import capo_sagemaker.types.code_repositories

        out["code_repositories"] = (
            capo_sagemaker.types.code_repositories.deserialize_aws_json_1_1(
                data["CodeRepositories"]
            )
        )
    if "AppLifecycleManagement" in data:
        import capo_sagemaker.types.space_app_lifecycle_management

        out["app_lifecycle_management"] = (
            capo_sagemaker.types.space_app_lifecycle_management.deserialize_aws_json_1_1(
                data["AppLifecycleManagement"]
            )
        )
    return out
