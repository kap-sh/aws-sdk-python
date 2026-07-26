"""Generated from Smithy shape ``com.amazonaws.sagemaker#JupyterServerAppSettings``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.code_repositories
    import capo_sagemaker.types.lifecycle_config_arns
    import capo_sagemaker.types.resource_spec


class JupyterServerAppSettings(TypedDict, closed=True):
    default_resource_spec: NotRequired[
        "capo_sagemaker.types.resource_spec.ResourceSpec"
    ]
    """<p>The default instance type and the Amazon Resource Name (ARN) of the default SageMaker AI image used by the JupyterServer app. If you use the <code>LifecycleConfigArns</code> parameter, then this parameter is also required.</p>"""
    lifecycle_config_arns: NotRequired[
        "capo_sagemaker.types.lifecycle_config_arns.LifecycleConfigArns"
    ]
    """<p> The Amazon Resource Name (ARN) of the Lifecycle Configurations attached to the JupyterServerApp. If you use this parameter, the <code>DefaultResourceSpec</code> parameter is also required.</p> <note> <p>To remove a Lifecycle Config, you must set <code>LifecycleConfigArns</code> to an empty list.</p> </note>"""
    code_repositories: NotRequired[
        "capo_sagemaker.types.code_repositories.CodeRepositories"
    ]
    """<p>A list of Git repositories that SageMaker AI automatically displays to users for cloning in the JupyterServer application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JupyterServerAppSettings) -> dict:
    out: dict = {}
    if "default_resource_spec" in value:
        import capo_sagemaker.types.resource_spec

        out["DefaultResourceSpec"] = (
            capo_sagemaker.types.resource_spec.serialize_aws_json_1_1(
                value["default_resource_spec"]
            )
        )
    if "lifecycle_config_arns" in value:
        import capo_sagemaker.types.lifecycle_config_arns

        out["LifecycleConfigArns"] = (
            capo_sagemaker.types.lifecycle_config_arns.serialize_aws_json_1_1(
                value["lifecycle_config_arns"]
            )
        )
    if "code_repositories" in value:
        import capo_sagemaker.types.code_repositories

        out["CodeRepositories"] = (
            capo_sagemaker.types.code_repositories.serialize_aws_json_1_1(
                value["code_repositories"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> JupyterServerAppSettings:
    out: JupyterServerAppSettings = {}  # type: ignore[typeddict-item]
    if "DefaultResourceSpec" in data:
        import capo_sagemaker.types.resource_spec

        out["default_resource_spec"] = (
            capo_sagemaker.types.resource_spec.deserialize_aws_json_1_1(
                data["DefaultResourceSpec"]
            )
        )
    if "LifecycleConfigArns" in data:
        import capo_sagemaker.types.lifecycle_config_arns

        out["lifecycle_config_arns"] = (
            capo_sagemaker.types.lifecycle_config_arns.deserialize_aws_json_1_1(
                data["LifecycleConfigArns"]
            )
        )
    if "CodeRepositories" in data:
        import capo_sagemaker.types.code_repositories

        out["code_repositories"] = (
            capo_sagemaker.types.code_repositories.deserialize_aws_json_1_1(
                data["CodeRepositories"]
            )
        )
    return out
