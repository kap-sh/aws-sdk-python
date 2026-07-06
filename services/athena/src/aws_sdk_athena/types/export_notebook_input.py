"""Generated from Smithy shape ``com.amazonaws.athena#ExportNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from aws_sdk_athena.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_athena.types.notebook_id


class ExportNotebookInput(TypedDict, closed=True):
    notebook_id: "aws_sdk_athena.types.notebook_id.NotebookId"
    """<p>The ID of the notebook to export.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportNotebookInput) -> dict:
    out: dict = {}
    out["NotebookId"] = value["notebook_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportNotebookInput:
    out: ExportNotebookInput = {}  # type: ignore[typeddict-item]
    if "NotebookId" in data:
        out["notebook_id"] = data["NotebookId"]
    else:
        raise DeserializationError("ExportNotebookInput.notebook_id required")
    return out
