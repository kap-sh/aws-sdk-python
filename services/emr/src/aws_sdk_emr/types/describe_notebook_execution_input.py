"""Generated from Smithy shape ``com.amazonaws.emr#DescribeNotebookExecutionInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr.types.xml_string_max_len256


class DescribeNotebookExecutionInput(TypedDict):
    notebook_execution_id: NotRequired[
        "aws_sdk_emr.types.xml_string_max_len256.XmlStringMaxLen256"
    ]
    """<p>The unique identifier of the notebook execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeNotebookExecutionInput) -> dict:
    out: dict = {}
    if "notebook_execution_id" in value:
        out["NotebookExecutionId"] = value["notebook_execution_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeNotebookExecutionInput:
    out: DescribeNotebookExecutionInput = {}  # type: ignore[typeddict-item]
    if "NotebookExecutionId" in data:
        out["notebook_execution_id"] = data["NotebookExecutionId"]
    return out
