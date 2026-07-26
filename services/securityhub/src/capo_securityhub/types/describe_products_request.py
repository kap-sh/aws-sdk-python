"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeProductsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.max_results
    import capo_securityhub.types.next_token
    import capo_securityhub.types.non_empty_string


class DescribeProductsRequest(TypedDict, closed=True):
    next_token: NotRequired["capo_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>DescribeProducts</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["capo_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return.</p>"""
    product_arn: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The ARN of the integration to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeProductsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeProductsRequest:
    out: DescribeProductsRequest = {}  # type: ignore[typeddict-item]
    return out
