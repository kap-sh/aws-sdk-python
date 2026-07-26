"""Generated from Smithy shape ``com.amazonaws.sagemaker#CreateNotebookInstanceLifecycleConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_config_arn


class CreateNotebookInstanceLifecycleConfigOutput(TypedDict, closed=True):
    notebook_instance_lifecycle_config_arn: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_arn.NotebookInstanceLifecycleConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotebookInstanceLifecycleConfigOutput) -> dict:
    out: dict = {}
    if "notebook_instance_lifecycle_config_arn" in value:
        out["NotebookInstanceLifecycleConfigArn"] = value[
            "notebook_instance_lifecycle_config_arn"
        ]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotebookInstanceLifecycleConfigOutput:
    out: CreateNotebookInstanceLifecycleConfigOutput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceLifecycleConfigArn" in data:
        out["notebook_instance_lifecycle_config_arn"] = data[
            "NotebookInstanceLifecycleConfigArn"
        ]
    return out
