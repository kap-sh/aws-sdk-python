"""Generated from Smithy shape ``com.amazonaws.qconnect#GetRecommendationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qconnect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qconnect.types.recommendation_list
    import capo_qconnect.types.recommendation_trigger_list


class GetRecommendationsResponse(TypedDict, closed=True):
    recommendations: "capo_qconnect.types.recommendation_list.RecommendationList"
    """<p>The recommendations.</p>"""
    triggers: NotRequired[
        "capo_qconnect.types.recommendation_trigger_list.RecommendationTriggerList"
    ]
    """<p>The triggers corresponding to recommendations.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRecommendationsResponse) -> dict:
    out: dict = {}
    import capo_qconnect.types.recommendation_list

    out["recommendations"] = capo_qconnect.types.recommendation_list.serialize_json(
        value["recommendations"]
    )
    if "triggers" in value:
        import capo_qconnect.types.recommendation_trigger_list

        out["triggers"] = (
            capo_qconnect.types.recommendation_trigger_list.serialize_json(
                value["triggers"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetRecommendationsResponse:
    out: GetRecommendationsResponse = {}  # type: ignore[typeddict-item]
    if "recommendations" in data:
        import capo_qconnect.types.recommendation_list

        out["recommendations"] = (
            capo_qconnect.types.recommendation_list.deserialize_json(
                data["recommendations"]
            )
        )
    else:
        raise DeserializationError(
            "GetRecommendationsResponse.recommendations required"
        )
    if "triggers" in data:
        import capo_qconnect.types.recommendation_trigger_list

        out["triggers"] = (
            capo_qconnect.types.recommendation_trigger_list.deserialize_json(
                data["triggers"]
            )
        )
    return out
