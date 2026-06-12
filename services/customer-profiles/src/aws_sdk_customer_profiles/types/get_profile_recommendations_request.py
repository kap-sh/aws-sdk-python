"""Generated from Smithy shape ``com.amazonaws.customerprofiles#GetProfileRecommendationsRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_customer_profiles.types.candidate_id_list
    import aws_sdk_customer_profiles.types.max_size500
    import aws_sdk_customer_profiles.types.metadata_config
    import aws_sdk_customer_profiles.types.name
    import aws_sdk_customer_profiles.types.recommender_context
    import aws_sdk_customer_profiles.types.recommender_filters
    import aws_sdk_customer_profiles.types.recommender_promotional_filters
    import aws_sdk_customer_profiles.types.uuid


class GetProfileRecommendationsRequest(TypedDict):
    domain_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""
    profile_id: "aws_sdk_customer_profiles.types.uuid.uuid"
    """<p>The unique identifier of the profile for which to retrieve recommendations.</p>"""
    recommender_name: "aws_sdk_customer_profiles.types.name.name"
    """<p>The unique name of the recommender.</p>"""
    context: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_context.RecommenderContext"
    ]
    """<p>The contextual metadata used to provide dynamic runtime information to tailor recommendations.</p>"""
    recommender_filters: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_filters.RecommenderFilters"
    ]
    """<p>A list of filters to apply to the returned recommendations. Filters define criteria for including or excluding items from the recommendation results.</p>"""
    recommender_promotional_filters: NotRequired[
        "aws_sdk_customer_profiles.types.recommender_promotional_filters.RecommenderPromotionalFilters"
    ]
    """<p>A list of promotional filters to apply to the recommendations. Promotional filters allow you to promote specific items within a configurable subset of recommendation results.</p>"""
    candidate_ids: NotRequired[
        "aws_sdk_customer_profiles.types.candidate_id_list.CandidateIdList"
    ]
    """<p>A list of item IDs to rank for the user. Use this when you want to re-rank a specific set of items rather than getting recommendations from the full item catalog. Required for personalized-ranking use cases.</p>"""
    max_results: NotRequired["aws_sdk_customer_profiles.types.max_size500.MaxSize500"]
    """<p>The maximum number of recommendations to return. The default value is 10.</p>"""
    metadata_config: NotRequired[
        "aws_sdk_customer_profiles.types.metadata_config.MetadataConfig"
    ]
    """<p>Configuration for including item metadata in the recommendation response. Use this to specify which metadata columns to return alongside recommended items.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetProfileRecommendationsRequest) -> dict:
    out: dict = {}
    out["RecommenderName"] = value["recommender_name"]
    if "context" in value:
        import aws_sdk_customer_profiles.types.recommender_context

        out["Context"] = (
            aws_sdk_customer_profiles.types.recommender_context.serialize_json(
                value["context"]
            )
        )
    if "recommender_filters" in value:
        import aws_sdk_customer_profiles.types.recommender_filters

        out["RecommenderFilters"] = (
            aws_sdk_customer_profiles.types.recommender_filters.serialize_json(
                value["recommender_filters"]
            )
        )
    if "recommender_promotional_filters" in value:
        import aws_sdk_customer_profiles.types.recommender_promotional_filters

        out["RecommenderPromotionalFilters"] = (
            aws_sdk_customer_profiles.types.recommender_promotional_filters.serialize_json(
                value["recommender_promotional_filters"]
            )
        )
    if "candidate_ids" in value:
        import aws_sdk_customer_profiles.types.candidate_id_list

        out["CandidateIds"] = (
            aws_sdk_customer_profiles.types.candidate_id_list.serialize_json(
                value["candidate_ids"]
            )
        )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "metadata_config" in value:
        import aws_sdk_customer_profiles.types.metadata_config

        out["MetadataConfig"] = (
            aws_sdk_customer_profiles.types.metadata_config.serialize_json(
                value["metadata_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetProfileRecommendationsRequest:
    out: GetProfileRecommendationsRequest = {}  # type: ignore[typeddict-item]
    if "RecommenderName" in data:
        out["recommender_name"] = data["RecommenderName"]
    else:
        raise DeserializationError(
            "GetProfileRecommendationsRequest.recommender_name required"
        )
    if "Context" in data:
        import aws_sdk_customer_profiles.types.recommender_context

        out["context"] = (
            aws_sdk_customer_profiles.types.recommender_context.deserialize_json(
                data["Context"]
            )
        )
    if "RecommenderFilters" in data:
        import aws_sdk_customer_profiles.types.recommender_filters

        out["recommender_filters"] = (
            aws_sdk_customer_profiles.types.recommender_filters.deserialize_json(
                data["RecommenderFilters"]
            )
        )
    if "RecommenderPromotionalFilters" in data:
        import aws_sdk_customer_profiles.types.recommender_promotional_filters

        out["recommender_promotional_filters"] = (
            aws_sdk_customer_profiles.types.recommender_promotional_filters.deserialize_json(
                data["RecommenderPromotionalFilters"]
            )
        )
    if "CandidateIds" in data:
        import aws_sdk_customer_profiles.types.candidate_id_list

        out["candidate_ids"] = (
            aws_sdk_customer_profiles.types.candidate_id_list.deserialize_json(
                data["CandidateIds"]
            )
        )
    if "MaxResults" in data:
        out["max_results"] = data["MaxResults"]
    if "MetadataConfig" in data:
        import aws_sdk_customer_profiles.types.metadata_config

        out["metadata_config"] = (
            aws_sdk_customer_profiles.types.metadata_config.deserialize_json(
                data["MetadataConfig"]
            )
        )
    return out
