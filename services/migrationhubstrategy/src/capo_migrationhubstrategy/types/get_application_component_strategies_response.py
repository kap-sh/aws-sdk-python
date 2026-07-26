"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetApplicationComponentStrategiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.application_component_strategies


class GetApplicationComponentStrategiesResponse(TypedDict, closed=True):
    application_component_strategies: NotRequired[
        "capo_migrationhubstrategy.types.application_component_strategies.ApplicationComponentStrategies"
    ]
    """<p> A list of application component strategy recommendations. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetApplicationComponentStrategiesResponse) -> dict:
    out: dict = {}
    if "application_component_strategies" in value:
        import capo_migrationhubstrategy.types.application_component_strategies

        out["applicationComponentStrategies"] = (
            capo_migrationhubstrategy.types.application_component_strategies.serialize_json(
                value["application_component_strategies"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetApplicationComponentStrategiesResponse:
    out: GetApplicationComponentStrategiesResponse = {}  # type: ignore[typeddict-item]
    if "applicationComponentStrategies" in data:
        import capo_migrationhubstrategy.types.application_component_strategies

        out["application_component_strategies"] = (
            capo_migrationhubstrategy.types.application_component_strategies.deserialize_json(
                data["applicationComponentStrategies"]
            )
        )
    return out
