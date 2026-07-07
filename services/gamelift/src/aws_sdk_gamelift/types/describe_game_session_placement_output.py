"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeGameSessionPlacementOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_session_placement


class DescribeGameSessionPlacementOutput(TypedDict, closed=True):
    game_session_placement: NotRequired[
        "aws_sdk_gamelift.types.game_session_placement.GameSessionPlacement"
    ]
    """<p>Object that describes the requested game session placement.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeGameSessionPlacementOutput) -> dict:
    out: dict = {}
    if "game_session_placement" in value:
        import aws_sdk_gamelift.types.game_session_placement

        out["GameSessionPlacement"] = (
            aws_sdk_gamelift.types.game_session_placement.serialize_aws_json_1_1(
                value["game_session_placement"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeGameSessionPlacementOutput:
    out: DescribeGameSessionPlacementOutput = {}  # type: ignore[typeddict-item]
    if "GameSessionPlacement" in data:
        import aws_sdk_gamelift.types.game_session_placement

        out["game_session_placement"] = (
            aws_sdk_gamelift.types.game_session_placement.deserialize_aws_json_1_1(
                data["GameSessionPlacement"]
            )
        )
    return out
