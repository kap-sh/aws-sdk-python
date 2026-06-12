"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.player

PlayerList: TypeAlias = list["aws_sdk_gamelift.types.player.Player"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerList) -> list:
    import aws_sdk_gamelift.types.player

    out: list = []
    for item in value:
        out.append(aws_sdk_gamelift.types.player.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerList:
    import aws_sdk_gamelift.types.player

    out: PlayerList = []
    for item in data:
        out.append(aws_sdk_gamelift.types.player.deserialize_aws_json_1_1(item))
    return out
