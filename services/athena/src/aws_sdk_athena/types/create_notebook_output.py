"""Generated from Smithy shape ``com.amazonaws.athena#CreateNotebookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_athena.types.notebook_id


class CreateNotebookOutput(TypedDict, closed=True):
    notebook_id: NotRequired["aws_sdk_athena.types.notebook_id.NotebookId"]
    """<p>A unique identifier for the notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateNotebookOutput) -> dict:
    out: dict = {}
    if "notebook_id" in value:
        out["NotebookId"] = value["notebook_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateNotebookOutput:
    out: CreateNotebookOutput = {}  # type: ignore[typeddict-item]
    if "NotebookId" in data:
        out["notebook_id"] = data["NotebookId"]
    return out
