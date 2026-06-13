"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteNotebookInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.notebook_id


class DeleteNotebookInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>"""
    identifier: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotebookInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotebookInput:
    out: DeleteNotebookInput = {}  # type: ignore[typeddict-item]
    return out
