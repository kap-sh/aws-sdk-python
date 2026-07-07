"""Generated from Smithy shape ``com.amazonaws.sagemaker#DescribeNotebookInstanceLifecycleConfigOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.creation_time
    import aws_sdk_sagemaker.types.last_modified_time
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_arn
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name


class DescribeNotebookInstanceLifecycleConfigOutput(TypedDict, closed=True):
    notebook_instance_lifecycle_config_arn: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_arn.NotebookInstanceLifecycleConfigArn"
    ]
    """<p>The Amazon Resource Name (ARN) of the lifecycle configuration.</p>"""
    notebook_instance_lifecycle_config_name: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_name.NotebookInstanceLifecycleConfigName"
    ]
    """<p>The name of the lifecycle configuration.</p>"""
    on_create: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list.NotebookInstanceLifecycleConfigList"
    ]
    """<p>The shell script that runs only once, when you create a notebook instance.</p>"""
    on_start: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list.NotebookInstanceLifecycleConfigList"
    ]
    """<p>The shell script that runs every time you start a notebook instance, including when you create the notebook instance.</p>"""
    last_modified_time: NotRequired[
        "aws_sdk_sagemaker.types.last_modified_time.LastModifiedTime"
    ]
    """<p>A timestamp that tells when the lifecycle configuration was last modified.</p>"""
    creation_time: NotRequired["aws_sdk_sagemaker.types.creation_time.CreationTime"]
    """<p>A timestamp that tells when the lifecycle configuration was created.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeNotebookInstanceLifecycleConfigOutput,
) -> dict:
    out: dict = {}
    if "notebook_instance_lifecycle_config_arn" in value:
        out["NotebookInstanceLifecycleConfigArn"] = value[
            "notebook_instance_lifecycle_config_arn"
        ]
    if "notebook_instance_lifecycle_config_name" in value:
        out["NotebookInstanceLifecycleConfigName"] = value[
            "notebook_instance_lifecycle_config_name"
        ]
    if "on_create" in value:
        import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list

        out["OnCreate"] = (
            aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list.serialize_aws_json_1_1(
                value["on_create"]
            )
        )
    if "on_start" in value:
        import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list

        out["OnStart"] = (
            aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list.serialize_aws_json_1_1(
                value["on_start"]
            )
        )
    if "last_modified_time" in value:
        import aws_sdk_sagemaker.types.last_modified_time

        out["LastModifiedTime"] = (
            aws_sdk_sagemaker.types.last_modified_time.serialize_aws_json_1_1(
                value["last_modified_time"]
            )
        )
    if "creation_time" in value:
        import aws_sdk_sagemaker.types.creation_time

        out["CreationTime"] = (
            aws_sdk_sagemaker.types.creation_time.serialize_aws_json_1_1(
                value["creation_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeNotebookInstanceLifecycleConfigOutput:
    out: DescribeNotebookInstanceLifecycleConfigOutput = {}  # type: ignore[typeddict-item]
    if "NotebookInstanceLifecycleConfigArn" in data:
        out["notebook_instance_lifecycle_config_arn"] = data[
            "NotebookInstanceLifecycleConfigArn"
        ]
    if "NotebookInstanceLifecycleConfigName" in data:
        out["notebook_instance_lifecycle_config_name"] = data[
            "NotebookInstanceLifecycleConfigName"
        ]
    if "OnCreate" in data:
        import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list

        out["on_create"] = (
            aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list.deserialize_aws_json_1_1(
                data["OnCreate"]
            )
        )
    if "OnStart" in data:
        import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list

        out["on_start"] = (
            aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_list.deserialize_aws_json_1_1(
                data["OnStart"]
            )
        )
    if "LastModifiedTime" in data:
        import aws_sdk_sagemaker.types.last_modified_time

        out["last_modified_time"] = (
            aws_sdk_sagemaker.types.last_modified_time.deserialize_aws_json_1_1(
                data["LastModifiedTime"]
            )
        )
    if "CreationTime" in data:
        import aws_sdk_sagemaker.types.creation_time

        out["creation_time"] = (
            aws_sdk_sagemaker.types.creation_time.deserialize_aws_json_1_1(
                data["CreationTime"]
            )
        )
    return out
