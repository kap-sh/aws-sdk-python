"""Generated from Smithy shape ``com.amazonaws.datazone#DeleteNotebookInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.notebook_id


class DeleteNotebookInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook exists.</p>"""
    identifier: "capo_datazone.types.notebook_id.NotebookId"
    """<p>The identifier of the notebook to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteNotebookInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DeleteNotebookInput:
    out: DeleteNotebookInput = {}  # type: ignore[typeddict-item]
    return out
