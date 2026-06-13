"""Generated from Smithy shape ``com.amazonaws.datazone#ListAssetFiltersInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.asset_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.filter_status
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token


class ListAssetFiltersInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain where you want to list asset filters.</p>"""
    asset_identifier: "aws_sdk_datazone.types.asset_id.AssetId"
    """<p>The ID of the data asset.</p>"""
    status: NotRequired["aws_sdk_datazone.types.filter_status.FilterStatus"]
    """<p>The status of the asset filter.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of asset filters is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of asset filters, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListAssetFilters</code> to list the next set of asset filters.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of asset filters to return in a single call to <code>ListAssetFilters</code>. When the number of asset filters to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListAssetFilters</code> to list the next set of asset filters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAssetFiltersInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListAssetFiltersInput:
    out: ListAssetFiltersInput = {}  # type: ignore[typeddict-item]
    return out
