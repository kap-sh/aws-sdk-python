"""Generated from Smithy shape ``com.amazonaws.costexplorer#GetRightsizingRecommendationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_cost_explorer.types.next_page_token
    import aws_sdk_cost_explorer.types.rightsizing_recommendation_configuration
    import aws_sdk_cost_explorer.types.rightsizing_recommendation_list
    import aws_sdk_cost_explorer.types.rightsizing_recommendation_metadata
    import aws_sdk_cost_explorer.types.rightsizing_recommendation_summary


class GetRightsizingRecommendationResponse(TypedDict):
    metadata: NotRequired[
        "aws_sdk_cost_explorer.types.rightsizing_recommendation_metadata.RightsizingRecommendationMetadata"
    ]
    """<p>Information regarding this specific recommendation set.</p>"""
    summary: NotRequired[
        "aws_sdk_cost_explorer.types.rightsizing_recommendation_summary.RightsizingRecommendationSummary"
    ]
    """<p>Summary of this recommendation set.</p>"""
    rightsizing_recommendations: NotRequired[
        "aws_sdk_cost_explorer.types.rightsizing_recommendation_list.RightsizingRecommendationList"
    ]
    """<p>Recommendations to rightsize resources.</p>"""
    next_page_token: NotRequired[
        "aws_sdk_cost_explorer.types.next_page_token.NextPageToken"
    ]
    """<p>The token to retrieve the next set of results.</p>"""
    configuration: NotRequired[
        "aws_sdk_cost_explorer.types.rightsizing_recommendation_configuration.RightsizingRecommendationConfiguration"
    ]
    """<p>You can use Configuration to customize recommendations across two attributes. You can choose to view recommendations for instances within the same instance families or across different instance families. You can also choose to view your estimated savings that are associated with recommendations with consideration of existing Savings Plans or RI benefits, or neither. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRightsizingRecommendationResponse) -> dict:
    out: dict = {}
    if "metadata" in value:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_metadata

        out["Metadata"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_metadata.serialize_aws_json_1_1(
                value["metadata"]
            )
        )
    if "summary" in value:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_summary

        out["Summary"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_summary.serialize_aws_json_1_1(
                value["summary"]
            )
        )
    if "rightsizing_recommendations" in value:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_list

        out["RightsizingRecommendations"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_list.serialize_aws_json_1_1(
                value["rightsizing_recommendations"]
            )
        )
    if "next_page_token" in value:
        out["NextPageToken"] = value["next_page_token"]
    if "configuration" in value:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_configuration

        out["Configuration"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRightsizingRecommendationResponse:
    out: GetRightsizingRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "Metadata" in data:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_metadata

        out["metadata"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_metadata.deserialize_aws_json_1_1(
                data["Metadata"]
            )
        )
    if "Summary" in data:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_summary

        out["summary"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_summary.deserialize_aws_json_1_1(
                data["Summary"]
            )
        )
    if "RightsizingRecommendations" in data:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_list

        out["rightsizing_recommendations"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_list.deserialize_aws_json_1_1(
                data["RightsizingRecommendations"]
            )
        )
    if "NextPageToken" in data:
        out["next_page_token"] = data["NextPageToken"]
    if "Configuration" in data:
        import aws_sdk_cost_explorer.types.rightsizing_recommendation_configuration

        out["configuration"] = (
            aws_sdk_cost_explorer.types.rightsizing_recommendation_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    return out
