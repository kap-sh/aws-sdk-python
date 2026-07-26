"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#ServerStrategy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.boolean
    import capo_migrationhubstrategy.types.integer
    import capo_migrationhubstrategy.types.recommendation_set
    import capo_migrationhubstrategy.types.strategy_recommendation


class ServerStrategy(TypedDict, closed=True):
    recommendation: NotRequired[
        "capo_migrationhubstrategy.types.recommendation_set.RecommendationSet"
    ]
    """<p> Strategy recommendation for the server. </p>"""
    status: NotRequired[
        "capo_migrationhubstrategy.types.strategy_recommendation.StrategyRecommendation"
    ]
    """<p> The recommendation status of the strategy for the server. </p>"""
    number_of_application_components: NotRequired[
        "capo_migrationhubstrategy.types.integer.Integer"
    ]
    """<p> The number of application components with this strategy recommendation running on the server. </p>"""
    is_preferred: NotRequired["capo_migrationhubstrategy.types.boolean.Boolean"]
    """<p> Set to true if the recommendation is set as preferred. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServerStrategy) -> dict:
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
    if "number_of_application_components" in value:
        out["numberOfApplicationComponents"] = value["number_of_application_components"]
    if "is_preferred" in value:
        out["isPreferred"] = value["is_preferred"]
    return out


def deserialize_json(data: dict) -> ServerStrategy:
    out: ServerStrategy = {}  # type: ignore[typeddict-item]
    if "recommendation" in data:
        import capo_migrationhubstrategy.types.recommendation_set

        out["recommendation"] = (
            capo_migrationhubstrategy.types.recommendation_set.deserialize_json(
                data["recommendation"]
            )
        )
    if "status" in data:
        out["status"] = data["status"]
    if "numberOfApplicationComponents" in data:
        out["number_of_application_components"] = data["numberOfApplicationComponents"]
    if "isPreferred" in data:
        out["is_preferred"] = data["isPreferred"]
    return out
