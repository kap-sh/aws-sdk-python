"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerConnectionEndpointList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.player_connection_endpoint

PlayerConnectionEndpointList: TypeAlias = list[
    "aws_sdk_gamelift.types.player_connection_endpoint.PlayerConnectionEndpoint"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerConnectionEndpointList) -> list:
    import aws_sdk_gamelift.types.player_connection_endpoint

    out: list = []
    for item in value:
        out.append(
            aws_sdk_gamelift.types.player_connection_endpoint.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> PlayerConnectionEndpointList:
    import aws_sdk_gamelift.types.player_connection_endpoint

    out: PlayerConnectionEndpointList = []
    for item in data:
        out.append(
            aws_sdk_gamelift.types.player_connection_endpoint.deserialize_aws_json_1_1(
                item
            )
        )
    return out
