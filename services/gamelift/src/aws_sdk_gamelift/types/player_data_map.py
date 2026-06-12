"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerDataMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.non_zero_and_max_string
    import aws_sdk_gamelift.types.player_data

PlayerDataMap: TypeAlias = dict[
    "aws_sdk_gamelift.types.non_zero_and_max_string.NonZeroAndMaxString",
    "aws_sdk_gamelift.types.player_data.PlayerData",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(input_to_serialize: PlayerDataMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerDataMap:
    out: PlayerDataMap = {}
    for key, value in data.items():
        out[key] = value
    return out
