"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.notebook_id


class GetNotebookInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>"""
    identifier: "aws_sdk_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotebookInput:
    out: GetNotebookInput = {}  # type: ignore[typeddict-item]
    return out
