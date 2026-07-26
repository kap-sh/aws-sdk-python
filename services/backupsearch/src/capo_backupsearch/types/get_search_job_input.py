"""Generated from Smithy shape ``com.amazonaws.backupsearch#GetSearchJobInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.generic_id


class GetSearchJobInput(TypedDict, closed=True):
    search_job_identifier: "capo_backupsearch.types.generic_id.GenericId"
    """<p>Required unique string that specifies the search job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetSearchJobInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> GetSearchJobInput:
    out: GetSearchJobInput = {}  # type: ignore[typeddict-item]
    return out
