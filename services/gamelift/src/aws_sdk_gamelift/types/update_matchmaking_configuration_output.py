"""Generated from Smithy shape ``com.amazonaws.gamelift#UpdateMatchmakingConfigurationOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_configuration


class UpdateMatchmakingConfigurationOutput(TypedDict):
    configuration: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_configuration.MatchmakingConfiguration"
    ]
    """<p>The updated matchmaking configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateMatchmakingConfigurationOutput) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_gamelift.types.matchmaking_configuration

        out["Configuration"] = (
            aws_sdk_gamelift.types.matchmaking_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateMatchmakingConfigurationOutput:
    out: UpdateMatchmakingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_gamelift.types.matchmaking_configuration

        out["configuration"] = (
            aws_sdk_gamelift.types.matchmaking_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    return out
