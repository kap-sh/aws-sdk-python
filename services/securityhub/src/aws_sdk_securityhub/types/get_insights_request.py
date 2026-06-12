"""Generated from Smithy shape ``com.amazonaws.securityhub#GetInsightsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.arn_list
    import aws_sdk_securityhub.types.max_results
    import aws_sdk_securityhub.types.next_token


class GetInsightsRequest(TypedDict):
    insight_arns: NotRequired["aws_sdk_securityhub.types.arn_list.ArnList"]
    """<p>The ARNs of the insights to describe. If you don't provide any insight ARNs, then <code>GetInsights</code> returns all of your custom insights. It does not return any managed insights.</p>"""
    next_token: NotRequired["aws_sdk_securityhub.types.next_token.NextToken"]
    """<p>The token that is required for pagination. On your first call to the <code>GetInsights</code> operation, set the value of this parameter to <code>NULL</code>.</p> <p>For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.</p>"""
    max_results: NotRequired["aws_sdk_securityhub.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetInsightsRequest) -> dict:
    out: dict = {}
    if "insight_arns" in value:
        import aws_sdk_securityhub.types.arn_list

        out["InsightArns"] = aws_sdk_securityhub.types.arn_list.serialize_json(
            value["insight_arns"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    return out


def deserialize_json(data: dict) -> GetInsightsRequest:
    out: GetInsightsRequest = {}  # type: ignore[typeddict-item]
    if "InsightArns" in data:
        import aws_sdk_securityhub.types.arn_list

        out["insight_arns"] = aws_sdk_securityhub.types.arn_list.deserialize_json(
            data["InsightArns"]
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    return out
