"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeVcenterClientsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mgn.types.max_results_type
    import capo_mgn.types.pagination_token


class DescribeVcenterClientsRequest(TypedDict, closed=True):
    max_results: NotRequired["capo_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum results to be returned in DescribeVcenterClients.</p>"""
    next_token: NotRequired["capo_mgn.types.pagination_token.PaginationToken"]
    """<p>Next pagination token to be provided for DescribeVcenterClients.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVcenterClientsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVcenterClientsRequest:
    out: DescribeVcenterClientsRequest = {}  # type: ignore[typeddict-item]
    return out
