"""Generated from Smithy shape ``com.amazonaws.sagemaker#DeleteNotebookInstanceLifecycleConfigInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_name


class DeleteNotebookInstanceLifecycleConfigInput(TypedDict, closed=True):
    notebook_instance_lifecycle_config_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>The name of the lifecycle configuration to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteNotebookInstanceLifecycleConfigInput) -> dict:
    out: dict = {}
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteNotebookInstanceLifecycleConfigInput:
    out: DeleteNotebookInstanceLifecycleConfigInput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceLifecycleConfigName" in data:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    return out
