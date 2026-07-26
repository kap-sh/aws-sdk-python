"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sagemaker.types.notebook_instance_lifecycle_hook

NotebookInstanceLifecycleConfigList: TypeAlias = list[
    "capo_sagemaker.types.notebook_instance_lifecycle_hook.NotebookInstanceLifecycleHook"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigList) -> list:
    import capo_sagemaker.types.notebook_instance_lifecycle_hook

    out: list = []
    for item in value:
        out.append(
            capo_sagemaker.types.notebook_instance_lifecycle_hook.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> NotebookInstanceLifecycleConfigList:
    import capo_sagemaker.types.notebook_instance_lifecycle_hook

    out: NotebookInstanceLifecycleConfigList = []
    for item in data:
        out.append(
            capo_sagemaker.types.notebook_instance_lifecycle_hook.deserialize_aws_json_1_1(
                item
            )
        )
    return out
