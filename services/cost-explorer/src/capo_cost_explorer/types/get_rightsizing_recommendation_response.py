"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetRightsizingRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cost_explorer.types.next_page_token
    import capo_cost_explorer.types.rightsizing_recommendation_configuration
    import capo_cost_explorer.types.rightsizing_recommendation_list
    import capo_cost_explorer.types.rightsizing_recommendation_metadata
    import capo_cost_explorer.types.rightsizing_recommendation_summary


class GetRightsizingRecommendationResponse(TypedDict, closed=True):
    metadata: NotRequired[
        "capo_cost_explorer.types.rightsizing_recommendation_metadata.RightsizingRecommendationMetadata"
    ]
    """<p>Information regarding this specific recommendation set.</p>"""
    summary: NotRequired[
        "capo_cost_explorer.types.rightsizing_recommendation_summary.RightsizingRecommendationSummary"
    ]
    """<p>Summary of this recommendation set.</p>"""
    rightsizing_recommendations: NotRequired[
        "capo_cost_explorer.types.rightsizing_recommendation_list.RightsizingRecommendationList"
    ]
    """<p>Recommendations to rightsize resources.</p>"""
    next_page_token: NotRequired[
        "capo_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""
    configuration: NotRequired[
        "capo_cost_explorer.types.rightsizing_recommendation_configuration.RightsizingRecommendationConfiguration"
    ]
    """<p>You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRightsizingRecommendationResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import capo_cost_explorer.types.rightsizing_recommendation_metadata

        out["Metadata"] = (
            capo_cost_explorer.types.rightsizing_recommendation_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "summary" in value:
        import capo_cost_explorer.types.rightsizing_recommendation_summary

        out["Summary"] = (
            capo_cost_explorer.types.rightsizing_recommendation_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    if "rightsizing_recommendations" in value:
        import capo_cost_explorer.types.rightsizing_recommendation_list

        out["RightsizingRecommendations"] = (
            capo_cost_explorer.types.rightsizing_recommendation_list.serialize_aws_json_1_1(
                value["rightsizing_recommendations"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "configuration" in value:
        import capo_cost_explorer.types.rightsizing_recommendation_configuration

        out["Configuration"] = (
            capo_cost_explorer.types.rightsizing_recommendation_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRightsizingRecommendationResponse:
    out: GetRightsizingRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import capo_cost_explorer.types.rightsizing_recommendation_metadata

        out["metadata"] = (
            capo_cost_explorer.types.rightsizing_recommendation_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if "Summary" in data:
        import capo_cost_explorer.types.rightsizing_recommendation_summary

        out["summary"] = (
            capo_cost_explorer.types.rightsizing_recommendation_summary.deserialize_aws_json_1_1(
                data["Summary"]
            )
        )
    if "RightsizingRecommendations" in data:
        import capo_cost_explorer.types.rightsizing_recommendation_list

        out["rightsizing_recommendations"] = (
            capo_cost_explorer.types.rightsizing_recommendation_list.deserialize_aws_json_1_1(
                data["RightsizingRecommendations"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "Configuration" in data:
        import capo_cost_explorer.types.rightsizing_recommendation_configuration

        out["configuration"] = (
            capo_cost_explorer.types.rightsizing_recommendation_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    return out
