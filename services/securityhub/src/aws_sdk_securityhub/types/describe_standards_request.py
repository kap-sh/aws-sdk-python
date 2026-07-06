"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeStandardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class DescribeStandardsRequest(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>DescribeStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of standards to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStandardsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeStandardsRequest:
    out: DescribeStandardsRequest = {}  # type: ignore[typeddict-item]
    return out
