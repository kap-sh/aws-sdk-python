"""Generated from Smithy shape ``com.amazonaws.emr#DescribeNotebookExecutionOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.notebook_execution


class DescribeNotebookExecutionOutput(TypedDict):
    notebook_execution: NotRequired[
        "aws_sdk_emr.types.notebook_execution.NotebookExecution"
    ]
    """<p>Properties of the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNotebookExecutionOutput) -> dict:
    out: dict = {}
    if "notebook_execution" in value:
        import aws_sdk_emr.types.notebook_execution

        out["NotebookExecution"] = (
            aws_sdk_emr.types.notebook_execution.serialize_aws_json_1_1(
                value["notebook_execution"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNotebookExecutionOutput:
    out: DescribeNotebookExecutionOutput = {}  # type: ignore[typeddict-item]
    if "NotebookExecution" in data:
        import aws_sdk_emr.types.notebook_execution

        out["notebook_execution"] = (
            aws_sdk_emr.types.notebook_execution.deserialize_aws_json_1_1(
                data["NotebookExecution"]
            )
        )
    return out
