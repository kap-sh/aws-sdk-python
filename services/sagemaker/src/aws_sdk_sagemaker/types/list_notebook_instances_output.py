"""Generated from Smithy shape ``com.amazonaws.sagemaker#ListNotebookInstancesOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sagemaker.types.next_token
    import aws_sdk_sagemaker.types.notebook_instance_summary_list


class ListNotebookInstancesOutput(TypedDict):
    next_token: NotRequired["aws_sdk_sagemaker.types.next_token.NextToken"]
    """<p>If the response to the previous <code>ListNotebookInstances</code> request was truncated, SageMaker AI returns this token. To retrieve the next set of notebook instances, use the token in the next request.</p>"""
    notebook_instances: NotRequired[
        "aws_sdk_sagemaker.types.notebook_instance_summary_list.NotebookInstanceSummaryList"
    ]
    """<p>An array of <code>NotebookInstanceSummary</code> objects, one for each notebook instance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookInstancesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "notebook_instances" in value:
        import aws_sdk_sagemaker.types.notebook_instance_summary_list

        out["NotebookInstances"] = (
            aws_sdk_sagemaker.types.notebook_instance_summary_list.serialize_aws_json_1_1(
                value["notebook_instances"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookInstancesOutput:
    out: ListNotebookInstancesOutput = {}  # type: ignore[typeddict-item]
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "NotebookInstances" in data:
        import aws_sdk_sagemaker.types.notebook_instance_summary_list

        out["notebook_instances"] = (
            aws_sdk_sagemaker.types.notebook_instance_summary_list.deserialize_aws_json_1_1(
                data["NotebookInstances"]
            )
        )
    return out
