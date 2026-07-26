"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerLatencyPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_gamelift.types.player_latency_policy

PlayerLatencyPolicyList: TypeAlias = list[
    "capo_gamelift.types.player_latency_policy.PlayerLatencyPolicy"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerLatencyPolicyList) -> list:
    import capo_gamelift.types.player_latency_policy

    out: list = []
    for item in value:
        out.append(
            capo_gamelift.types.player_latency_policy.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerLatencyPolicyList:
    import capo_gamelift.types.player_latency_policy

    out: PlayerLatencyPolicyList = []
    for item in data:
        out.append(
            capo_gamelift.types.player_latency_policy.deserialize_aws_json_1_1(item)
        )
    return out
