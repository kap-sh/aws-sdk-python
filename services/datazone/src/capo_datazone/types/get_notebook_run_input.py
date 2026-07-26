"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookRunInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_run_id


class GetNotebookRunInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook run exists.</p>"""
    identifier: "capo_datazone.types.notebook_run_id.NotebookRunId"
    """<p>The identifier of the notebook run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookRunInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotebookRunInput:
    out: GetNotebookRunInput = {}  # type: ignore[typeddict-item]
    return out
