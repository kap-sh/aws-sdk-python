"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ListAppComponentRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.component_recommendation_list
    import aws_sdk_resiliencehub.types.next_token


class ListAppComponentRecommendationsResponse(TypedDict):
    component_recommendations: "aws_sdk_resiliencehub.types.component_recommendation_list.ComponentRecommendationList"
    """<p>The recommendations for an Resilience Hub Application Component, returned as an object. This object contains the names of the Application Components, configuration recommendations, and recommendation statuses.</p>"""
    next_token: NotRequired["aws_sdk_resiliencehub.types.next_token.NextToken"]
    """<p>Token for the next set of results, or null if there are no more results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListAppComponentRecommendationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_resiliencehub.types.component_recommendation_list

    out["componentRecommendations"] = (
        aws_sdk_resiliencehub.types.component_recommendation_list.serialize_json(
            value["component_recommendations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListAppComponentRecommendationsResponse:
    out: ListAppComponentRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "componentRecommendations" in data:
        import aws_sdk_resiliencehub.types.component_recommendation_list

        out["component_recommendations"] = (
            aws_sdk_resiliencehub.types.component_recommendation_list.deserialize_json(
                data["componentRecommendations"]
            )
        )
    else:
        raise DeserializationError(
            "ListAppComponentRecommendationsResponse.component_recommendations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
