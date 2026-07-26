"""Generated from Smithy shape ``com.amazonaws.athena#ImportNotebookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.notebook_id


class ImportNotebookOutput(TypedDict, closed=True):
    notebook_id: NotRequired["capo_athena.types.notebook_id.NotebookId"]
    """<p>The ID assigned to the imported notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImportNotebookOutput) -> dict:
    out: dict = {}
    if "notebook_id" in value:
        out["NotebookId"] = value["notebook_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImportNotebookOutput:
    out: ImportNotebookOutput = {}  # type: ignore[typeddict-item]
    if "NotebookId" in data:
        out["notebook_id"] = data["NotebookId"]
    return out
