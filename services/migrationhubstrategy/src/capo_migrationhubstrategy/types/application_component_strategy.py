"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ApplicationComponentStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.boolean
    import capo_migrationhubstrategy.types.recommendation_set
    import capo_migrationhubstrategy.types.strategy_recommendation


class ApplicationComponentStrategy(TypedDict, closed=True):
    recommendation: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_set.RecommendationSet"
    ]
    """<p> Strategy recommendation for the application component. </p>"""
    status: NotRequired[
        "capo_migrationhubstrategy.types.strategy_recommendation.StrategyRecommendation"
    ]
    """<p> The recommendation status of a strategy for an application component. </p>"""
    is_preferred: NotRequired["capo_migrationhubstrategy.types.boolean.Boolean"]
    """<p> Set to true if the recommendation is set as preferred. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ApplicationComponentStrategy) -> dict:
    out: dict = {}
    if "recommendation" in value:
        import capo_migrationhubstrategy.types.recommendation_set

        out["recommendation"] = (
            capo_migrationhubstrategy.types.recommendation_set.serialize_json(
                value["recommendation"]
            )
        )
    if "status" in value:
        out["status"] = value["status"]
    if "is_preferred" in value:
        out["isPreferred"] = value["is_preferred"]
    return out


def deserialize_json(data: dict) -> ApplicationComponentStrategy:
    out: ApplicationComponentStrategy = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import capo_migrationhubstrategy.types.recommendation_set

        out["recommendation"] = (
            capo_migrationhubstrategy.types.recommendation_set.deserialize_json(
                data["recommendation"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "isPreferred" in data:
        out["is_preferred"] = data["isPreferred"]
    return out
