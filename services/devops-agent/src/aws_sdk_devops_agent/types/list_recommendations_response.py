"""Generated from Smithy shape ``com.amazonaws.devopsagent#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.recommendation_list


class ListRecommendationsResponse(TypedDict, closed=True):
    recommendations: "aws_sdk_devops_agent.types.recommendation_list.RecommendationList"
    """<p>List of recommendations matching the request criteria</p>"""
    next_token: NotRequired["str"]
    """<p>Token for retrieving the next page of results, if more results are available</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.recommendation_list

    out["recommendations"] = (
        aws_sdk_devops_agent.types.recommendation_list.serialize_json(
            value["recommendations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "recommendations" in data:
        import aws_sdk_devops_agent.types.recommendation_list

        out["recommendations"] = (
            aws_sdk_devops_agent.types.recommendation_list.deserialize_json(
                data["recommendations"]
            )
        )
    else:
        raise DeserializationError(
            "ListRecommendationsResponse.recommendations required"
        )
    if "nextToken" in data:
        out["next_token"] = data["nextToken"]
    return out
