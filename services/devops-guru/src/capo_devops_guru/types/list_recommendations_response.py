"""Generated from Smithy shape ``com.amazonaws.devopsguru#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_devops_guru.types.recommendations
    import capo_devops_guru.types.uuid_next_token


class ListRecommendationsResponse(TypedDict, closed=True):
    recommendations: NotRequired[
        "capo_devops_guru.types.recommendations.Recommendations"
    ]
    """<p> An array of the requested recommendations. </p>"""
    next_token: NotRequired["capo_devops_guru.types.uuid_next_token.UuidNextToken"]
    """<p>The pagination token to use to retrieve the next page of results for this operation. If there are no more pages, this value is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    if "recommendations" in value:
        import capo_devops_guru.types.recommendations

        out["Recommendations"] = capo_devops_guru.types.recommendations.serialize_json(
            value["recommendations"]
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "Recommendations" in data:
        import capo_devops_guru.types.recommendations

        out["recommendations"] = (
            capo_devops_guru.types.recommendations.deserialize_json(
                data["Recommendations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
