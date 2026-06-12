"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateGameServerOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server


class UpdateGameServerOutput(TypedDict):
    game_server: NotRequired["aws_sdk_gamelift.types.game_server.GameServer"]
    """<p>Object that describes the newly updated game server.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateGameServerOutput) -> dict:
    out: dict = {}
    if "game_server" in value:
        import aws_sdk_gamelift.types.game_server

        out["GameServer"] = aws_sdk_gamelift.types.game_server.serialize_aws_json_1_1(
            value["game_server"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateGameServerOutput:
    out: UpdateGameServerOutput = {}  # type: ignore[typeddict-item]
    if "GameServer" in data:
        import aws_sdk_gamelift.types.game_server

        out["game_server"] = (
            aws_sdk_gamelift.types.game_server.deserialize_aws_json_1_1(
                data["GameServer"]
            )
        )
    return out
