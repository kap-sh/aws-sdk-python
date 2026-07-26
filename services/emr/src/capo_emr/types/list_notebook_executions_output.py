"""Generated from Smithy shape ``com.amazonaws.emr#ListNotebookExecutionsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.marker
    import capo_emr.types.notebook_execution_summary_list


class ListNotebookExecutionsOutput(TypedDict, closed=True):
    notebook_executions: NotRequired[
        "capo_emr.types.notebook_execution_summary_list.NotebookExecutionSummaryList"
    ]
    """<p>A list of notebook executions.</p>"""
    marker: NotRequired["capo_emr.types.marker.Marker"]
    """<p>A pagination token that a subsequent <code>ListNotebookExecutions</code> can use to determine the next set of results to retrieve.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListNotebookExecutionsOutput) -> dict:
    out: dict = {}
    if "notebook_executions" in value:
        import capo_emr.types.notebook_execution_summary_list

        out["NotebookExecutions"] = (
            capo_emr.types.notebook_execution_summary_list.serialize_aws_json_1_1(
                value["notebook_executions"]
            )
        )
    if "marker" in value:
        out["Marker"] = value["marker"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ListNotebookExecutionsOutput:
    out: ListNotebookExecutionsOutput = {}  # type: ignore[typeddict-item]
    if "NotebookExecutions" in data:
        import capo_emr.types.notebook_execution_summary_list

        out["notebook_executions"] = (
            capo_emr.types.notebook_execution_summary_list.deserialize_aws_json_1_1(
                data["NotebookExecutions"]
            )
        )
    if "Marker" in data:
        out["marker"] = data["Marker"]
    return out
