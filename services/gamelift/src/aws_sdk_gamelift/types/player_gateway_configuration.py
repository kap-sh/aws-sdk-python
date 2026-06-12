"""Generated from Smithy shape ``com.amazonaws.gamelift#PlayerGatewayConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_gamelift.types.game_server_ip_protocol_supported


class PlayerGatewayConfiguration(TypedDict):
    game_server_ip_protocol_supported: NotRequired[
        "aws_sdk_gamelift.types.game_server_ip_protocol_supported.GameServerIpProtocolSupported"
    ]
    """<p>The IP protocol that your game servers support for player connections through player gateway. If the value is set to <code>IPv4</code>, GameLift will install and execute a lightweight IP translation software on fleet instances to receive and transform incoming IPv6 traffic to IPv4. If the value is set to <code>DUAL_STACK</code>, the lightweight IP translation software will not be installed on fleet instances. <code>DUAL_STACK</code> provides slightly better performance than <code>IPv4</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PlayerGatewayConfiguration) -> dict:
    out: dict = {}
    if "game_server_ip_protocol_supported" in value:
        import aws_sdk_gamelift.types.game_server_ip_protocol_supported

        out["GameServerIpProtocolSupported"] = (
            aws_sdk_gamelift.types.game_server_ip_protocol_supported.serialize_aws_json_1_1(
                value["game_server_ip_protocol_supported"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PlayerGatewayConfiguration:
    out: PlayerGatewayConfiguration = {}  # type: ignore[typeddict-item]
    if "GameServerIpProtocolSupported" in data:
        import aws_sdk_gamelift.types.game_server_ip_protocol_supported

        out["game_server_ip_protocol_supported"] = (
            aws_sdk_gamelift.types.game_server_ip_protocol_supported.deserialize_aws_json_1_1(
                data["GameServerIpProtocolSupported"]
            )
        )
    return out
