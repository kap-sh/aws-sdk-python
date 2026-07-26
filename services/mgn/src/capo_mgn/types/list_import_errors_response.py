"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportErrorsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.import_errors
    import capo_mgn.types.pagination_token


class ListImportErrorsResponse(TypedDict, closed=True):
    items: NotRequired["capo_mgn.types.import_errors.ImportErrors"]
    """<p>List imports errors response items.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>List imports errors response next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportErrorsResponse) -> dict:
    out: dict = {}
    if "items" in value:
        import capo_mgn.types.import_errors

        out["items"] = capo_mgn.types.import_errors.serialize_json(value["items"])
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportErrorsResponse:
    out: ListImportErrorsResponse = {}  # type: ignore[typeddict-item]
    if "items" in data:
        import capo_mgn.types.import_errors

        out["items"] = capo_mgn.types.import_errors.deserialize_json(data["items"])
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
