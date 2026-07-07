"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListNotebookInstanceLifecycleConfigsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_summary_list


class ListNotebookInstanceLifecycleConfigsOutput(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response is truncated, SageMaker AI returns this token. To get the next set of lifecycle configurations, use it in the next request. </p>"""
    notebook_instance_lifecycle_configs: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_summary_list.NotebookInstanceLifecycleConfigSummaryList"
    ]
    """<p>An array of <code>NotebookInstanceLifecycleConfiguration</code> objects, each listing a lifecycle configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookInstanceLifecycleConfigsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "notebook_instance_lifecycle_configs" in value:
        import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_summary_list

        out["NotebookInstanceLifecycleConfigs"] = (
            aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_summary_list.serialize_aws_json_1_1(
                value["notebook_instance_lifecycle_configs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookInstanceLifecycleConfigsOutput:
    out: ListNotebookInstanceLifecycleConfigsOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NotebookInstanceLifecycleConfigs" in data:
        import aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_summary_list

        out["notebook_instance_lifecycle_configs"] = (
            aws_sdk_sagemaker.types.notebook_instance_lifecycle_config_summary_list.deserialize_aws_json_1_1(
                data["NotebookInstanceLifecycleConfigs"]
            )
        )
    return out
