"""Generated from Smithy shape ``com.amazonaws.athena#GetNotebookMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.notebook_metadata


class GetNotebookMetadataOutput(TypedDict, closed=True):
    notebook_metadata: NotRequired[
        "capo_athena.types.notebook_metadata.NotebookMetadata"
    ]
    """<p>The metadata that is returned for the specified notebook ID.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetNotebookMetadataOutput) -> dict:
    out: dict = {}
    if "notebook_metadata" in value:
        import capo_athena.types.notebook_metadata

        out["NotebookMetadata"] = (
            capo_athena.types.notebook_metadata.serialize_aws_json_1_1(
                value["notebook_metadata"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetNotebookMetadataOutput:
    out: GetNotebookMetadataOutput = {}  # type: ignore[typeddict-item]
    if "NotebookMetadata" in data:
        import capo_athena.types.notebook_metadata

        out["notebook_metadata"] = (
            capo_athena.types.notebook_metadata.deserialize_aws_json_1_1(
                data["NotebookMetadata"]
            )
        )
    return out
