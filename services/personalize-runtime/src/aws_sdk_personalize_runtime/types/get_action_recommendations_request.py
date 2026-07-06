"""Generated from Smithy shape ``com.amazonaws.personalizeruntime#GetActionRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_personalize_runtime.types.arn
    import aws_sdk_personalize_runtime.types.filter_values
    import aws_sdk_personalize_runtime.types.num_results
    import aws_sdk_personalize_runtime.types.user_id


class GetActionRecommendationsRequest(TypedDict, closed=True):
    campaign_arn: NotRequired["aws_sdk_personalize_runtime.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) of the campaign to use for getting action recommendations. This campaign must deploy a solution version trained with a PERSONALIZED_ACTIONS recipe.</p>"""
    user_id: NotRequired["aws_sdk_personalize_runtime.types.user_id.UserID"]
    """<p>The user ID of the user to provide action recommendations for.</p>"""
    num_results: "aws_sdk_personalize_runtime.types.num_results.NumResults"
    """<p>The number of results to return. The default is 5. The maximum is 100.</p>"""
    filter_arn: NotRequired["aws_sdk_personalize_runtime.types.arn.Arn"]
    r"""<p>The ARN of the filter to apply to the returned recommendations. For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/filter.html\">Filtering Recommendations</a>.</p> <p>When using this parameter, be sure the filter resource is <code>ACTIVE</code>.</p>"""
    filter_values: NotRequired[
        "aws_sdk_personalize_runtime.types.filter_values.FilterValues"
    ]
    r"""<p>The values to use when filtering recommendations. For each placeholder parameter in your filter expression, provide the parameter name (in matching case) as a key and the filter value(s) as the corresponding value. Separate multiple values for one parameter with a comma. </p> <p>For filter expressions that use an <code>INCLUDE</code> element to include actions, you must provide values for all parameters that are defined in the expression. For filters with expressions that use an <code>EXCLUDE</code> element to exclude actions, you can omit the <code>filter-values</code>. In this case, Amazon Personalize doesn't use that portion of the expression to filter recommendations.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/personalize/latest/dg/filter.html\">Filtering recommendations and user segments</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetActionRecommendationsRequest) -> dict:
    out: dict = {}
    if "campaign_arn" in value:
        out["campaignArn"] = value["campaign_arn"]
    if "user_id" in value:
        out["userId"] = value["user_id"]
    out["numResults"] = value.get("num_results", 0)
    if "filter_arn" in value:
        out["filterArn"] = value["filter_arn"]
    if "filter_values" in value:
        import aws_sdk_personalize_runtime.types.filter_values

        out["filterValues"] = (
            aws_sdk_personalize_runtime.types.filter_values.serialize_json(
                value["filter_values"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetActionRecommendationsRequest:
    out: GetActionRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "campaignArn" in data:
        out["campaign_arn"] = data["campaignArn"]
    if "userId" in data:
        out["user_id"] = data["userId"]
    if "numResults" in data:
        out["num_results"] = data["numResults"]
    else:
        out["num_results"] = 0
    if "filterArn" in data:
        out["filter_arn"] = data["filterArn"]
    if "filterValues" in data:
        import aws_sdk_personalize_runtime.types.filter_values

        out["filter_values"] = (
            aws_sdk_personalize_runtime.types.filter_values.deserialize_json(
                data["filterValues"]
            )
        )
    return out
