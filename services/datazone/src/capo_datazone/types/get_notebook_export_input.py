"""Generated from Smithy shape ``com.amazonaws.datazone#GetNotebookExportInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.domain_id
    import capo_datazone.types.export_id


class GetNotebookExportInput(TypedDict, closed=True):
    domain_identifier: "capo_datazone.types.domain_id.DomainId"
    """<p>The identifier of the Amazon SageMaker Unified Studio domain in which the notebook export exists.</p>"""
    identifier: "capo_datazone.types.export_id.ExportId"
    """<p>The identifier of the notebook export.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNotebookExportInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetNotebookExportInput:
    out: GetNotebookExportInput = {}  # type: ignore[typeddict-item]
    return out
