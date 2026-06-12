"""Generated from Smithy shape ``com.amazonaws.athena#ExportNotebookOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.notebook_metadata
    import aws_sdk_athena.types.payload


class ExportNotebookOutput(TypedDict):
    notebook_metadata: NotRequired[
        "aws_sdk_athena.types.notebook_metadata.NotebookMetadata"
    ]
    """<p>The notebook metadata, including notebook ID, notebook name, and workgroup name.</p>"""
    payload: NotRequired["aws_sdk_athena.types.payload.Payload"]
    """<p>The content of the exported notebook.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExportNotebookOutput) -> dict:
    out: dict = {}
    if "notebook_metadata" in value:
        import aws_sdk_athena.types.notebook_metadata

        out["NotebookMetadata"] = (
            aws_sdk_athena.types.notebook_metadata.serialize_aws_json_1_1(
                value["notebook_metadata"]
            )
        )
    if "payload" in value:
        out["Payload"] = value["payload"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExportNotebookOutput:
    out: ExportNotebookOutput = {}  # type: ignore[typeddict-item]
    if "NotebookMetadata" in data:
        import aws_sdk_athena.types.notebook_metadata

        out["notebook_metadata"] = (
            aws_sdk_athena.types.notebook_metadata.deserialize_aws_json_1_1(
                data["NotebookMetadata"]
            )
        )
    if "Payload" in data:
        out["payload"] = data["Payload"]
    return out
