"""Generated from Smithy shape ``com.amazonaws.emr#StopNotebookExecutionInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr.types.xml_string_max_len256


class StopNotebookExecutionInput(TypedDict, closed=True):
    notebook_execution_id: NotRequired[
        "capo_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopNotebookExecutionInput) -> dict:
    out: dict = {}
    if "notebook_execution_id" in value:
        out["NotebookExecutionId"] = value["notebook_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopNotebookExecutionInput:
    out: StopNotebookExecutionInput = {}  # type: ignore[typeddict-item]
    if "NotebookExecutionId" in data:
        out["notebook_execution_id"] = data["NotebookExecutionId"]
    return out
