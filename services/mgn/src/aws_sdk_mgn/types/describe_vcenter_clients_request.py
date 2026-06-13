"""Generated from Smithy shape ``com.amazonaws.mgn#DescribeVcenterClientsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mgn.types.max_results_type
    import aws_sdk_mgn.types.pagination_token


class DescribeVcenterClientsRequest(TypedDict):
    max_results: NotRequired["aws_sdk_mgn.types.max_results_type.MaxResultsType"]
    """<p>Maximum results to be returned in DescribeVcenterClients.</p>"""
    next_token: NotRequired["aws_sdk_mgn.types.pagination_token.PaginationToken"]
    """<p>Next pagination token to be provided for DescribeVcenterClients.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeVcenterClientsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeVcenterClientsRequest:
    out: DescribeVcenterClientsRequest = {}  # type: ignore[typeddict-item]
    return out
