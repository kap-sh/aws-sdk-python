"""Generated from Smithy shape ``com.amazonaws.sesv2#ListRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_sesv2.types.next_token
    import aws_sdk_sesv2.types.recommendations_list


class ListRecommendationsResponse(TypedDict):
    recommendations: NotRequired[
        "aws_sdk_sesv2.types.recommendations_list.RecommendationsList"
    ]
    """<p>The recommendations applicable to your account.</p>"""
    next_token: NotRequired["aws_sdk_sesv2.types.next_token.NextToken"]
    """<p>A string token indicating that there might be additional recommendations available to be listed. Use the token provided in the <code>ListRecommendationsResponse</code> to use in the subsequent call to <code>ListRecommendations</code> with the same parameters to retrieve the next page of recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecommendationsResponse) -> dict:
    out: dict = {}
    if "recommendations" in value:
        import aws_sdk_sesv2.types.recommendations_list

        out["Recommendations"] = (
            aws_sdk_sesv2.types.recommendations_list.serialize_json(
                value["recommendations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecommendationsResponse:
    out: ListRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "Recommendations" in data:
        import aws_sdk_sesv2.types.recommendations_list

        out["recommendations"] = (
            aws_sdk_sesv2.types.recommendations_list.deserialize_json(
                data["Recommendations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
