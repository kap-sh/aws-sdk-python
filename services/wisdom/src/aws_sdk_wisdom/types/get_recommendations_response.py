"""Generated from Smithy shape ``com.amazonaws.wisdom#GetRecommendationsResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_wisdom.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_wisdom.types.recommendation_list
    import aws_sdk_wisdom.types.recommendation_trigger_list


class GetRecommendationsResponse(TypedDict):
    recommendations: "aws_sdk_wisdom.types.recommendation_list.RecommendationList"
    """<p>The recommendations.</p>"""
    triggers: NotRequired[
        "aws_sdk_wisdom.types.recommendation_trigger_list.RecommendationTriggerList"
    ]
    """<p>The triggers corresponding to recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsResponse) -> dict:
    out: dict = {}
    import aws_sdk_wisdom.types.recommendation_list

    out["recommendations"] = aws_sdk_wisdom.types.recommendation_list.serialize_json(
        value["recommendations"]
    )
    if "triggers" in value:
        import aws_sdk_wisdom.types.recommendation_trigger_list

        out["triggers"] = (
            aws_sdk_wisdom.types.recommendation_trigger_list.serialize_json(
                value["triggers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationsResponse:
    out: GetRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "recommendations" in data:
        import aws_sdk_wisdom.types.recommendation_list

        out["recommendations"] = (
            aws_sdk_wisdom.types.recommendation_list.deserialize_json(
                data["recommendations"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationsResponse.recommendations required"
        )
    if "triggers" in data:
        import aws_sdk_wisdom.types.recommendation_trigger_list

        out["triggers"] = (
            aws_sdk_wisdom.types.recommendation_trigger_list.deserialize_json(
                data["triggers"]
            )
        )
    return out
