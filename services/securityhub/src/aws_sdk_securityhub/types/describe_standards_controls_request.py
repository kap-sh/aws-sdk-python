"""Generated from Smithy shape ``com.amazonaws.securityhub#DescribeStandardsControlsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.non_empty_string


class DescribeStandardsControlsRequest(TypedDict):
    standards_subscription_arn: (
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    )
    """<p>The ARN of a resource that represents your subscription to a supported standard. To get the subscription ARNs of the standards you have enabled, use the <code>GetEnabledStandards</code> operation.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>DescribeStandardsControls</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of security standard controls to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeStandardsControlsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> DescribeStandardsControlsRequest:
    out: DescribeStandardsControlsRequest = {}  # type: ignore[typeddict-item]
    return out
