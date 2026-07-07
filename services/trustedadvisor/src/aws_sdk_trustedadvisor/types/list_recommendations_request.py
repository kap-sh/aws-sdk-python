"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#ListRecommendationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import aws_sdk_trustedadvisor.types.check_identifier
    import aws_sdk_trustedadvisor.types.recommendation_aws_service
    import aws_sdk_trustedadvisor.types.recommendation_language
    import aws_sdk_trustedadvisor.types.recommendation_pillar
    import aws_sdk_trustedadvisor.types.recommendation_source
    import aws_sdk_trustedadvisor.types.recommendation_status
    import aws_sdk_trustedadvisor.types.recommendation_type


class ListRecommendationsRequest(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results. </p>"""
    max_results: NotRequired["int"]
    """<p>The maximum number of results to return per page.</p>"""
    type: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_type.RecommendationType"
    ]
    """<p>The type of the Recommendation</p>"""
    status: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_status.RecommendationStatus"
    ]
    """<p>The status of the Recommendation</p>"""
    pillar: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_pillar.RecommendationPillar"
    ]
    """<p>The pillar of the Recommendation</p>"""
    aws_service: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_aws_service.RecommendationAwsService"
    ]
    """<p>The aws service associated with the Recommendation</p>"""
    source: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_source.RecommendationSource"
    ]
    """<p>The source of the Recommendation</p>"""
    check_identifier: NotRequired[
        "aws_sdk_trustedadvisor.types.check_identifier.CheckIdentifier"
    ]
    """<p>The check identifier of the Recommendation</p>"""
    after_last_updated_at: NotRequired["datetime.datetime"]
    """<p>After the last update of the Recommendation</p>"""
    before_last_updated_at: NotRequired["datetime.datetime"]
    """<p>Before the last update of the Recommendation</p>"""
    language: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation_language.RecommendationLanguage"
    ]
    """<p>The ISO 639-1 code for the language that you want your recommendations to appear in.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListRecommendationsRequest:
    out: ListRecommendationsRequest = {}  # type: ignore[typeddict-item]
    return out
