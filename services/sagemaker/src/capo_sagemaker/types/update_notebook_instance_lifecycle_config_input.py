"""Generated from Smithy shape ``com.amazonaws.sagemaker#UpdateNotebookInstanceLifecycleConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_list
    import capo_sagemaker.types.notebook_instance_lifecycle_config_name


class UpdateNotebookInstanceLifecycleConfigInput(TypedDict, closed=True):
    notebook_instance_lifecycle_config_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>The name of the lifecycle configuration.</p>"""
    on_create: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_list.NotebookInstanceLifecycleConfigList"
    ]
    """<p>The shell script that runs only once, when you create a notebook instance. The shell script must be a base64-encoded string.</p>"""
    on_start: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_list.NotebookInstanceLifecycleConfigList"
    ]
    """<p>The shell script that runs every time you start a notebook instance, including when you create the notebook instance. The shell script must be a base64-encoded string.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateNotebookInstanceLifecycleConfigInput) -> dict:
    out: dict = {}
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    if "on_create" in value:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["OnCreate"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.serialize_aws_json_1_1(
                value["on_create"]
            )
        )
    if "on_start" in value:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["OnStart"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.serialize_aws_json_1_1(
                value["on_start"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateNotebookInstanceLifecycleConfigInput:
    out: UpdateNotebookInstanceLifecycleConfigInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceLifecycleConfigName" in data:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    if "OnCreate" in data:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["on_create"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.deserialize_aws_json_1_1(
                data["OnCreate"]
            )
        )
    if "OnStart" in data:
        import capo_sagemaker.types.notebook_instance_lifecycle_config_list

        out["on_start"] = (
            capo_sagemaker.types.notebook_instance_lifecycle_config_list.deserialize_aws_json_1_1(
                data["OnStart"]
            )
        )
    return out
