"""Generated from Smithy shape ``com.amazonaws.athena#ExportNotebookOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.notebook_metadata
    import capo_athena.types.payload


class ExportNotebookOutput(TypedDict, closed=True):
    notebook_metadata: NotRequired[
        "capo_athena.types.notebook_metadata.NotebookMetadata"
    ]
    """<p>The notebook metadata, including notebook ID, notebook name, and workgroup name.</p>"""
    payload: NotRequired["capo_athena.types.payload.Payload"]
    """<p>The content of the exported notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportNotebookOutput) -> dict:
    out: dict = {}
    if "notebook_metadata" in value:
        import capo_athena.types.notebook_metadata

        out["NotebookMetadata"] = (
            capo_athena.types.notebook_metadata.serialize_aws_json_1_1(
                value["notebook_metadata"]
            )
        )
    if "payload" in value:
        out["Payload"] = value["payload"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportNotebookOutput:
    out: ExportNotebookOutput = {}  # type: ignore[typeddict-item]
    if "NotebookMetadata" in data:
        import capo_athena.types.notebook_metadata

        out["notebook_metadata"] = (
            capo_athena.types.notebook_metadata.deserialize_aws_json_1_1(
                data["NotebookMetadata"]
            )
        )
    if "Payload" in data:
        out["payload"] = data["Payload"]
    return out
