"""Generated from Smithy shape ``com.amazonaws.securityhub#GetEnabledStandardsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token
    import aws_sdk_securityhub.types.standards_subscription_arns


class GetEnabledStandardsRequest(TypedDict, closed=True):
    standards_subscription_arns: NotRequired[
        "aws_sdk_securityhub.types.standards_subscription_arns.StandardsSubscriptionArns"
    ]
    """<p>The list of the standards subscription ARNs for the standards to retrieve.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>GetEnabledStandards</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of results to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetEnabledStandardsRequest) -> dict:
    out: dict = {}
    if "standards_subscription_arns" in value:
        import aws_sdk_securityhub.types.standards_subscription_arns

        out["StandardsSubscriptionArns"] = (
            aws_sdk_securityhub.types.standards_subscription_arns.serialize_json(
                value["standards_subscription_arns"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetEnabledStandardsRequest:
    out: GetEnabledStandardsRequest = {}  # type: ignore[typeddict-item]
    if "StandardsSubscriptionArns" in data:
        import aws_sdk_securityhub.types.standards_subscription_arns

        out["standards_subscription_arns"] = (
            aws_sdk_securityhub.types.standards_subscription_arns.deserialize_json(
                data["StandardsSubscriptionArns"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
