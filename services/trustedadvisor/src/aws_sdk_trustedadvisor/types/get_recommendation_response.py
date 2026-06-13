"""Generated from Smithy shape ``com.amazonaws.trustedadvisor#GetRecommendationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_trustedadvisor.types.recommendation


class GetRecommendationResponse(TypedDict):
    recommendation: NotRequired[
        "aws_sdk_trustedadvisor.types.recommendation.Recommendation"
    ]
    """<p>The Recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationResponse) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import aws_sdk_trustedadvisor.types.recommendation

        out["recommendation"] = (
            aws_sdk_trustedadvisor.types.recommendation.serialize_json(
                value["recommendation"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationResponse:
    out: GetRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import aws_sdk_trustedadvisor.types.recommendation

        out["recommendation"] = (
            aws_sdk_trustedadvisor.types.recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    return out
