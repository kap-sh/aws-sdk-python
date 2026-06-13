"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookRunInput``."""

from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.notebook_run_id


class GetNotebookRunInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>"""
    identifier: "aws_sdk_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotebookRunInput:
    out: GetNotebookRunInput = {}  # type: ignore[typeddict-item]
    return out
