"""Generated from Smithy shape ``com.amazonaws.omics#GetRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.run_export_list
    import capo_omics.types.run_id


class GetRunRequest(TypedDict, closed=True):
    id: "capo_omics.types.run_id.RunId"
    """<p>The run's ID.</p>"""
    export: NotRequired["capo_omics.types.run_export_list.RunExportList"]
    """<p>The run's export format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRunRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetRunRequest:
    out: GetRunRequest = {}  # type: ignore[typeddict-item]
    return out
