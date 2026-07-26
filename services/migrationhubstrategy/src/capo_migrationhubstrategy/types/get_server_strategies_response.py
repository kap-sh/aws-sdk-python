"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#GetServerStrategiesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.server_strategies


class GetServerStrategiesResponse(TypedDict, closed=True):
    server_strategies: NotRequired[
        "capo_migrationhubstrategy.types.server_strategies.ServerStrategies"
    ]
    """<p> A list of strategy recommendations for the server. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServerStrategiesResponse) -> dict:
    out: dict = {}
    if "server_strategies" in value:
        import capo_migrationhubstrategy.types.server_strategies

        out["serverStrategies"] = (
            capo_migrationhubstrategy.types.server_strategies.serialize_json(
                value["server_strategies"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetServerStrategiesResponse:
    out: GetServerStrategiesResponse = {}  # type: ignore[typeddict-item]
    if "serverStrategies" in data:
        import capo_migrationhubstrategy.types.server_strategies

        out["server_strategies"] = (
            capo_migrationhubstrategy.types.server_strategies.deserialize_json(
                data["serverStrategies"]
            )
        )
    return out
