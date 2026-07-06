"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListTestRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.next_token
    import aws_sdk_resiliencehub.types.test_recommendation_list


class ListTestRecommendationsResponse(TypedDict, closed=True):
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""
    test_recommendations: (
        "aws_sdk_resiliencehub.types.test_recommendation_list.TestRecommendationList"
    )
    """<p>The test recommendations for the Resilience Hub application.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTestRecommendationsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import aws_sdk_resiliencehub.types.test_recommendation_list

    out["testRecommendations"] = (
        aws_sdk_resiliencehub.types.test_recommendation_list.serialize_json(
            value["test_recommendations"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListTestRecommendationsResponse:
    out: ListTestRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    if "testRecommendations" in data:
        import aws_sdk_resiliencehub.types.test_recommendation_list

        out["test_recommendations"] = (
            aws_sdk_resiliencehub.types.test_recommendation_list.deserialize_json(
                data["testRecommendations"]
            )
        )
    else:
        raise DeserializationError(
            "ListTestRecommendationsResponse.test_recommendations required"
        )
    return out
