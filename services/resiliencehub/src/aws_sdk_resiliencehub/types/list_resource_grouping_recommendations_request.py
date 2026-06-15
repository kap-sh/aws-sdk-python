"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListResourceGroupingRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.arn
    import aws_sdk_resiliencehub.types.max_results
    import aws_sdk_resiliencehub.types.next_token


class ListResourceGroupingRecommendationsRequest(TypedDict):
    app_arn: NotRequired["aws_sdk_resiliencehub.types.arn.Arn"]
    r"""<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href=\"https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html\"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Null, or the token from a previous call to get the next set of results.</p>"""
    max_results: NotRequired["aws_sdk_resiliencehub.types.max_results.MaxResults"]
    """<p>Maximum number of grouping recommendations to be displayed per Resilience Hub application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListResourceGroupingRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListResourceGroupingRecommendationsRequest:
    out: ListResourceGroupingRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
