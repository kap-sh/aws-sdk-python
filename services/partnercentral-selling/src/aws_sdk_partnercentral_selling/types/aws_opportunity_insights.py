"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AwsOpportunityInsights``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_partnercentral_selling.types.aws_products_spend_insights_by_source
    import aws_sdk_partnercentral_selling.types.engagement_score


class AwsOpportunityInsights(TypedDict):
    next_best_actions: NotRequired["str"]
    """<p>Provides recommendations from AWS on the next best actions to take in order to move the opportunity forward and increase the likelihood of success.</p>"""
    engagement_score: NotRequired[
        "aws_sdk_partnercentral_selling.types.engagement_score.EngagementScore"
    ]
    """<p>Represents a score assigned by AWS to indicate the level of engagement and potential success for the opportunity. This score helps partners prioritize their efforts.</p>"""
    aws_products_spend_insights_by_source: NotRequired[
        "aws_sdk_partnercentral_selling.types.aws_products_spend_insights_by_source.AwsProductsSpendInsightsBySource"
    ]
    """<p>Source-separated spend insights that provide independent analysis for AWS recommendations and partner estimates.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AwsOpportunityInsights) -> dict:
    out: dict = {}
    if "next_best_actions" in value:
        out["NextBestActions"] = value["next_best_actions"]
    if "engagement_score" in value:
        import aws_sdk_partnercentral_selling.types.engagement_score

        out["EngagementScore"] = (
            aws_sdk_partnercentral_selling.types.engagement_score.serialize_aws_json_1_0(
                value["engagement_score"]
            )
        )
    if "aws_products_spend_insights_by_source" in value:
        import aws_sdk_partnercentral_selling.types.aws_products_spend_insights_by_source

        out["AwsProductsSpendInsightsBySource"] = (
            aws_sdk_partnercentral_selling.types.aws_products_spend_insights_by_source.serialize_aws_json_1_0(
                value["aws_products_spend_insights_by_source"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> AwsOpportunityInsights:
    out: AwsOpportunityInsights = {}  # type: ignore[typeddict-item]
    if "NextBestActions" in data:
        out["next_best_actions"] = data["NextBestActions"]
    if "EngagementScore" in data:
        import aws_sdk_partnercentral_selling.types.engagement_score

        out["engagement_score"] = (
            aws_sdk_partnercentral_selling.types.engagement_score.deserialize_aws_json_1_0(
                data["EngagementScore"]
            )
        )
    if "AwsProductsSpendInsightsBySource" in data:
        import aws_sdk_partnercentral_selling.types.aws_products_spend_insights_by_source

        out["aws_products_spend_insights_by_source"] = (
            aws_sdk_partnercentral_selling.types.aws_products_spend_insights_by_source.deserialize_aws_json_1_0(
                data["AwsProductsSpendInsightsBySource"]
            )
        )
    return out
