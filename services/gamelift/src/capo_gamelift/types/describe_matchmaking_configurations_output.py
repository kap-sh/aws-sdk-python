"""Generated from Smithy shape ``com.amazonaws.gamelift#DescribeMatchmakingConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.matchmaking_configuration_list
    import capo_gamelift.types.non_zero_and_max_string


class DescribeMatchmakingConfigurationsOutput(TypedDict, closed=True):
    configurations: NotRequired[
        "capo_gamelift.types.matchmaking_configuration_list.MatchmakingConfigurationList"
    ]
    """<p>A collection of requested matchmaking configurations.</p>"""
    next_token: NotRequired[
        "capo_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString"
    ]
    """<p>A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeMatchmakingConfigurationsOutput) -> dict:
    out: dict = {}
    if "configurations" in value:
        import capo_gamelift.types.matchmaking_configuration_list

        out["Configurations"] = (
            capo_gamelift.types.matchmaking_configuration_list.serialize_aws_json_1_1(
                value["configurations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeMatchmakingConfigurationsOutput:
    out: DescribeMatchmakingConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if "Configurations" in data:
        import capo_gamelift.types.matchmaking_configuration_list

        out["configurations"] = (
            capo_gamelift.types.matchmaking_configuration_list.deserialize_aws_json_1_1(
                data["Configurations"]
            )
        )
    if "NextToken" in data:
        out["next_token"] = data["NextToken"]
    return out
