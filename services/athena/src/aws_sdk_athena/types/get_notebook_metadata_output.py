"""Generated from Smithy shape ``com.amazonaws.athena#GetNotebookMetadataOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_athena.types.notebook_metadata


class GetNotebookMetadataOutput(TypedDict):
    notebook_metadata: NotRequired[
        "aws_sdk_athena.types.notebook_metadata.NotebookMetadata"
    ]
    """<p>The metadata that is returned for the specified notebook ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNotebookMetadataOutput) -> dict:
    out: dict = {}
    if "notebook_metadata" in value:
        import aws_sdk_athena.types.notebook_metadata

        out["NotebookMetadata"] = (
            aws_sdk_athena.types.notebook_metadata.serialize_aws_json_1_1(
                value["notebook_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNotebookMetadataOutput:
    out: GetNotebookMetadataOutput = {}  # type: ignore[typeddict-item]
    if "NotebookMetadata" in data:
        import aws_sdk_athena.types.notebook_metadata

        out["notebook_metadata"] = (
            aws_sdk_athena.types.notebook_metadata.deserialize_aws_json_1_1(
                data["NotebookMetadata"]
            )
        )
    return out
