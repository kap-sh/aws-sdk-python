"""Generated from Smithy shape ``com.amazonaws.devopsagent#GetRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.recommendation


class GetRecommendationResponse(TypedDict, closed=True):
    recommendation: "capo_devops_agent.types.recommendation.Recommendation"
    """<p>The requested recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.recommendation

    out["recommendation"] = capo_devops_agent.types.recommendation.serialize_json(
        value["recommendation"]
    )
    return out


def deserialize_json(data: dict) -> GetRecommendationResponse:
    out: GetRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import capo_devops_agent.types.recommendation

        out["recommendation"] = capo_devops_agent.types.recommendation.deserialize_json(
            data["recommendation"]
        )
    else:
        raise DeserializationError("GetRecommendationResponse.recommendation required")
    return out
