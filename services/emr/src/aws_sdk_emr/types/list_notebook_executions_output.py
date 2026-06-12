"""Generated from Smithy shape ``com.amazonaws.emr#ListNotebookExecutionsOutput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.marker
    import aws_sdk_emr.types.notebook_execution_summary_list


class ListNotebookExecutionsOutput(TypedDict):
    notebook_executions: NotRequired[
        "aws_sdk_emr.types.notebook_execution_summary_list.NotebookExecutionSummaryList"
    ]
    """<p>A list of notebook executions.</p>"""
    marker: NotRequired["aws_sdk_emr.types.marker.Marker"]
    """<p>A pagination token that a subsequent <code>ListNotebookExecutions</code> can use to determine the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookExecutionsOutput) -> dict:
    out: dict = {}
    if "notebook_executions" in value:
        import aws_sdk_emr.types.notebook_execution_summary_list

        out["NotebookExecutions"] = (
            aws_sdk_emr.types.notebook_execution_summary_list.serialize_aws_json_1_1(
                value["notebook_executions"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookExecutionsOutput:
    out: ListNotebookExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "NotebookExecutions" in data:
        import aws_sdk_emr.types.notebook_execution_summary_list

        out["notebook_executions"] = (
            aws_sdk_emr.types.notebook_execution_summary_list.deserialize_aws_json_1_1(
                data["NotebookExecutions"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
