"""Generated from Smithy shape ``com.amazonaws.mgn#ListImportsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.list_imports_request_filters
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class ListImportsRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_mgn.types.list_imports_request_filters.ListImportsRequestFilters"
    ]
    """<p>List imports request filters.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>List imports request max results.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>List imports request next token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListImportsRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_mgn.types.list_imports_request_filters

        out["filters"] = aws_sdk_mgn.types.list_imports_request_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListImportsRequest:
    out: ListImportsRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_mgn.types.list_imports_request_filters

        out["filters"] = (
            aws_sdk_mgn.types.list_imports_request_filters.deserialize_json(
                data["filters"]
            )
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
