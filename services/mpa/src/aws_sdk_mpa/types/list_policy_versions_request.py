"""Generated from Smithy shape ``com.amazonaws.mpa#ListPolicyVersionsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_mpa.types.max_results
    import aws_sdk_mpa.types.token
    import aws_sdk_mpa.types.unqualified_policy_arn


class ListPolicyVersionsRequest(TypedDict):
    max_results: "aws_sdk_mpa.types.max_results.MaxResults"
    """<p>The maximum number of items to return in the response. If more results exist than the specified <code>MaxResults</code> value, a token is included in the response so that you can retrieve the remaining results.</p>"""
    next_token: NotRequired["aws_sdk_mpa.types.token.Token"]
    """<p>If present, indicates that more output is available than is included in the current response. Use this value in the <code>NextToken</code> request parameter in a next call to the operation to get more output. You can repeat this until the <code>NextToken</code> response element returns <code>null</code>.</p>"""
    policy_arn: "aws_sdk_mpa.types.unqualified_policy_arn.UnqualifiedPolicyArn"
    """<p>Amazon Resource Name (ARN) for the policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListPolicyVersionsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListPolicyVersionsRequest:
    out: ListPolicyVersionsRequest = {}  # type: ignore[typeddict-item]
    return out
