"""Generated from Smithy shape ``com.amazonaws.devopsagent#UpdateRecommendationResponse``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_devops_agent.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_devops_agent.types.recommendation


class UpdateRecommendationResponse(TypedDict):
    recommendation: "aws_sdk_devops_agent.types.recommendation.Recommendation"
    """<p>The updated recommendation</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateRecommendationResponse) -> dict:
    out: dict = {}
    import aws_sdk_devops_agent.types.recommendation

    out["recommendation"] = aws_sdk_devops_agent.types.recommendation.serialize_json(
        value["recommendation"]
    )
    return out


def deserialize_json(data: dict) -> UpdateRecommendationResponse:
    out: UpdateRecommendationResponse = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import aws_sdk_devops_agent.types.recommendation

        out["recommendation"] = (
            aws_sdk_devops_agent.types.recommendation.deserialize_json(
                data["recommendation"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateRecommendationResponse.recommendation required"
        )
    return out
