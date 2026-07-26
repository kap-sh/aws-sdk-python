"""Generated from Smithy shape ``com.amazonaws.mgn#ListExportErrorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_mgn.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mgn.types.export_id
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class ListExportErrorsRequest(TypedDict, closed=True):
    export_id: "capo_mgn.types.export_id.ExportID"
    """<p>List export errors request export id.</p>"""
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>List export errors request max results.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List export errors request next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExportErrorsRequest) -> dict:
    out: dict = {}
    out["exportID"] = value["export_id"]
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExportErrorsRequest:
    out: ListExportErrorsRequest = {}  # type: ignore[typeddict-item]
    if "exportID" in data:
        out["export_id"] = data["exportID"]
    else:
        raise DeserializationError("ListExportErrorsRequest.export_id required")
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
