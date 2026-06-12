"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerLatencyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.player_latency

PlayerLatencyList: TypeAlias = list[
    "aws_sdk_gamelift.types.player_latency.PlayerLatency"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerLatencyList) -> list:
    import aws_sdk_gamelift.types.player_latency

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.player_latency.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerLatencyList:
    import aws_sdk_gamelift.types.player_latency

    out: PlayerLatencyList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.player_latency.deserialize_aws_json_1_1(item))
    return out
