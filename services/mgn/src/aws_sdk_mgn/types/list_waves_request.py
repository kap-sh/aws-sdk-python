"""Generated from Smithy shape ``com.amazonaws.mgn#ListWavesRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_mgn.types.account_id
    import aws_sdk_mgn.types.list_waves_request_filters
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class ListWavesRequest(TypedDict, closed=True):
    filters: NotRequired[
        "aws_sdk_mgn.types.list_waves_request_filters.ListWavesRequestFilters"
    ]
    """<p>Waves list filters.</p>"""
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum results to return when listing waves.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Request next token.</p>"""
    account_id: NotRequired["aws_sdk_mgn.types.account_id.AccountID"]
    """<p>Request account ID.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWavesRequest) -> dict:
    out: dict = {}
    if "filters" in value:
        import aws_sdk_mgn.types.list_waves_request_filters

        out["filters"] = aws_sdk_mgn.types.list_waves_request_filters.serialize_json(
            value["filters"]
        )
    if "max_results" in value:
        out["maxResults"] = value["max_results"]
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    if "account_id" in value:
        out["accountID"] = value["account_id"]
    return out


def deserialize_json(data: dict) -> ListWavesRequest:
    out: ListWavesRequest = {}  # type: ignore[typeddict-item]
    if "filters" in data:
        import aws_sdk_mgn.types.list_waves_request_filters

        out["filters"] = aws_sdk_mgn.types.list_waves_request_filters.deserialize_json(
            data["filters"]
        )
    if "maxResults" in data:
        out["max_results"] = data["maxResults"]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "accountID" in data:
        out["account_id"] = data["accountID"]
    return out
