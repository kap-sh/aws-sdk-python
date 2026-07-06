"""Generated from Smithy shape ``com.amazonaws.gamelift#CreateMatchmakingConfigurationOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.matchmaking_configuration


class CreateMatchmakingConfigurationOutput(TypedDict, closed=True):
    configuration: NotRequired[
        "aws_sdk_gamelift.types.matchmaking_configuration.MatchmakingConfiguration"
    ]
    """<p>Object that describes the newly created matchmaking configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateMatchmakingConfigurationOutput) -> dict:
    out: dict = {}
    if "configuration" in value:
        import aws_sdk_gamelift.types.matchmaking_configuration

        out["Configuration"] = (
            aws_sdk_gamelift.types.matchmaking_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateMatchmakingConfigurationOutput:
    out: CreateMatchmakingConfigurationOutput = {}  # type: ignore[typeddict-item]
    if "Configuration" in data:
        import aws_sdk_gamelift.types.matchmaking_configuration

        out["configuration"] = (
            aws_sdk_gamelift.types.matchmaking_configuration.deserialize_aws_json_1_1(
                data["Configuration"]
            )
        )
    return out
