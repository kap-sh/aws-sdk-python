"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#UpdateServerConfigRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_migrationhubstrategy.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_migrationhubstrategy.types.server_id
    import aws_sdk_migrationhubstrategy.types.strategy_option


class UpdateServerConfigRequest(TypedDict):
    server_id: "aws_sdk_migrationhubstrategy.types.server_id.ServerId"
    """<p> The ID of the server. </p>"""
    strategy_option: NotRequired[
        "aws_sdk_migrationhubstrategy.types.strategy_option.StrategyOption"
    ]
    """<p> The preferred strategy options for the application component. See the response from <a>GetServerStrategies</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateServerConfigRequest) -> dict:
    out: dict = {}
    out["serverId"] = value["server_id"]
    if "strategy_option" in value:
        import aws_sdk_migrationhubstrategy.types.strategy_option

        out["strategyOption"] = (
            aws_sdk_migrationhubstrategy.types.strategy_option.serialize_json(
                value["strategy_option"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateServerConfigRequest:
    out: UpdateServerConfigRequest = {}  # type: ignore[typeddict-item]
    if "serverId" in data:
        out["server_id"] = data["serverId"]
    else:
        raise DeserializationError("UpdateServerConfigRequest.server_id required")
    if "strategyOption" in data:
        import aws_sdk_migrationhubstrategy.types.strategy_option

        out["strategy_option"] = (
            aws_sdk_migrationhubstrategy.types.strategy_option.deserialize_json(
                data["strategyOption"]
            )
        )
    return out
