"""Generated from Smithy shape ``com.amazonaws.gamelift#StopGameSessionPlacementOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_placement


class StopGameSessionPlacementOutput(TypedDict):
    game_session_placement: NotRequired[
        "aws_sdk_gamelift.types.game_session_placement.GameSessionPlacement"
    ]
    """<p>Object that describes the canceled game session placement, with <code>CANCELLED</code> status and an end time stamp. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopGameSessionPlacementOutput) -> dict:
    out: dict = {}
    if "game_session_placement" in value:
        import aws_sdk_gamelift.types.game_session_placement

        out["GameSessionPlacement"] = (
            aws_sdk_gamelift.types.game_session_placement.serialize_aws_json_1_1(
                value["game_session_placement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> StopGameSessionPlacementOutput:
    out: StopGameSessionPlacementOutput = {}  # type: ignore[typeddict-item]
    if "GameSessionPlacement" in data:
        import aws_sdk_gamelift.types.game_session_placement

        out["game_session_placement"] = (
            aws_sdk_gamelift.types.game_session_placement.deserialize_aws_json_1_1(
                data["GameSessionPlacement"]
            )
        )
    return out
