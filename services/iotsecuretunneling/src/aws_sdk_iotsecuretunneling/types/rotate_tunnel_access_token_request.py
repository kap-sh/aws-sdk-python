"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#RotateTunnelAccessTokenRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_iotsecuretunneling.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.client_mode
    import aws_sdk_iotsecuretunneling.types.destination_config
    import aws_sdk_iotsecuretunneling.types.tunnel_id


class RotateTunnelAccessTokenRequest(TypedDict):
    tunnel_id: "aws_sdk_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The tunnel for which you want to rotate the access tokens.</p>"""
    client_mode: "aws_sdk_iotsecuretunneling.types.client_mode.ClientMode"
    """<p>The mode of the client that will use the client token, which can be either the source or destination, or both source and destination.</p>"""
    destination_config: NotRequired[
        "aws_sdk_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateTunnelAccessTokenRequest) -> dict:
    out: dict = {}
    import aws_sdk_iotsecuretunneling.types.client_mode

    out["clientMode"] = (
        aws_sdk_iotsecuretunneling.types.client_mode.serialize_aws_json_1_1(
            value["client_mode"]
        )
    )
    if "destination_config" in value:
        import aws_sdk_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            aws_sdk_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateTunnelAccessTokenRequest:
    out: RotateTunnelAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if "clientMode" in data:
        import aws_sdk_iotsecuretunneling.types.client_mode

        out["client_mode"] = (
            aws_sdk_iotsecuretunneling.types.client_mode.deserialize_aws_json_1_1(
                data["clientMode"]
            )
        )
    else:
        raise DeserializationError(
            "RotateTunnelAccessTokenRequest.client_mode required"
        )
    if "destinationConfig" in data:
        import aws_sdk_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            aws_sdk_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    return out
