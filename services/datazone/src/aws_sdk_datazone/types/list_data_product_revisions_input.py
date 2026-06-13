"""Generated from Smithy shape ``com.amazonaws.datazone#ListDataProductRevisionsInput``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.data_product_id
    import aws_sdk_datazone.types.domain_id
    import aws_sdk_datazone.types.max_results
    import aws_sdk_datazone.types.pagination_token


class ListDataProductRevisionsInput(TypedDict):
    domain_identifier: "aws_sdk_datazone.types.domain_id.DomainId"
    """<p>The ID of the domain of the data product revisions that you want to list.</p>"""
    identifier: "aws_sdk_datazone.types.data_product_id.DataProductId"
    """<p>The ID of the data product revision.</p>"""
    max_results: NotRequired["aws_sdk_datazone.types.max_results.MaxResults"]
    """<p>The maximum number of asset filters to return in a single call to <code>ListDataProductRevisions</code>. When the number of data product revisions to be listed is greater than the value of <code>MaxResults</code>, the response contains a <code>NextToken</code> value that you can use in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>"""
    next_token: NotRequired["aws_sdk_datazone.types.pagination_token.PaginationToken"]
    """<p>When the number of data product revisions is greater than the default value for the <code>MaxResults</code> parameter, or if you explicitly specify a value for <code>MaxResults</code> that is less than the number of data product revisions, the response includes a pagination token named <code>NextToken</code>. You can specify this <code>NextToken</code> value in a subsequent call to <code>ListDataProductRevisions</code> to list the next set of data product revisions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListDataProductRevisionsInput) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListDataProductRevisionsInput:
    out: ListDataProductRevisionsInput = {}  # type: ignore[typeddict-item]
    return out
