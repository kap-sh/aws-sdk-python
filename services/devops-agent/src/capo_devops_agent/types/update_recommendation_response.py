"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateRecommendationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_devops_agent.types.recommendation


class UpdateRecommendationResponse(TypedDict, closed=True):
    recommendation: "capo_devops_agent.types.recommendation.Recommendation"
    """<p>The updated recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationResponse) -> dict:
    out: dict = {}
    import capo_devops_agent.types.recommendation

    out["recommendation"] = capo_devops_agent.types.recommendation.serialize_json(
        value["recommendation"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRecommendationResponse:
    out: UpdateRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import capo_devops_agent.types.recommendation

        out["recommendation"] = capo_devops_agent.types.recommendation.deserialize_json(
            data["recommendation"]
        )
    else:
        raise DeserializationError(
            "UpdateRecommendationResponse.recommendation required"
        )
    return out
