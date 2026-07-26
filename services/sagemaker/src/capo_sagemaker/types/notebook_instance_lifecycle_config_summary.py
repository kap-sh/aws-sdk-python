"""Generated from Smithy shape ``com.amazonaws.sagemaker#NotebookInstanceLifecycleConfigSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_sagemaker.types.creation_time
    import capo_sagemaker.types.last_modified_time
    import capo_sagemaker.types.notebook_instance_lifecycle_config_arn
    import capo_sagemaker.types.notebook_instance_lifecycle_config_name


class NotebookInstanceLifecycleConfigSummary(TypedDict, closed=True):
    notebook_instance_lifecycle_config_name: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>The name of the lifecycle configuration.</p>"""
    notebook_instance_lifecycle_config_arn: NotRequired[
        "capo_sagemaker.types.notebook_instance_lifecycle_config_arn.NotebookInstanceLifecycleConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle configuration.</p>"""
    creation_time: NotRequired["capo_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that tells when the lifecycle configuration was created.</p>"""
    last_modified_time: NotRequired[
        "capo_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp that tells when the lifecycle configuration was last modified.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NotebookInstanceLifecycleConfigSummary) -> dict:
    out: dict = {}
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    if "notebook_instance_lifecycle_config_arn" in value:
        out["NotebookInstanceLifecycleConfigArn"] = value[
            "notebook_instance_lifecycle_config_arn"
        ]
    if "creation_time" in value:
        import capo_sagemaker.types.creation_time

        out["CreationTime"] = capo_sagemaker.types.creation_time.serialize_aws_json_1_1(
            value["creation_time"]
        )
    if "last_modified_time" in value:
        import capo_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            capo_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NotebookInstanceLifecycleConfigSummary:
    out: NotebookInstanceLifecycleConfigSummary = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceLifecycleConfigName" in data:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    if "NotebookInstanceLifecycleConfigArn" in data:
        out["notebook_instance_lifecycle_config_arn"] = data[
            "NotebookInstanceLifecycleConfigArn"
        ]
    if "CreationTime" in data:
        import capo_sagemaker.types.creation_time

        out["creation_time"] = (
            capo_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    if "LastModifiedTime" in data:
        import capo_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            capo_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    return out
