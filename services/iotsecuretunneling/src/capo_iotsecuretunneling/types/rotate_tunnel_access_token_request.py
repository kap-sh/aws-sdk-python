"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#RotateTunnelAccessTokenRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotsecuretunneling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotsecuretunneling.types.client_mode
    import capo_iotsecuretunneling.types.destination_config
    import capo_iotsecuretunneling.types.tunnel_id


class RotateTunnelAccessTokenRequest(TypedDict, closed=True):
    tunnel_id: "capo_iotsecuretunneling.types.tunnel_id.TunnelId"
    """<p>The tunnel for which you want to rotate the access tokens.</p>"""
    client_mode: "capo_iotsecuretunneling.types.client_mode.ClientMode"
    """<p>The mode of the client that will use the client token, which can be either the source or destination, or both source and destination.</p>"""
    destination_config: NotRequired[
        "capo_iotsecuretunneling.types.destination_config.DestinationConfig"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateTunnelAccessTokenRequest) -> dict:
    out: dict = {}
    import capo_iotsecuretunneling.types.client_mode

    out["clientMode"] = (
        capo_iotsecuretunneling.types.client_mode.serialize_aws_json_1_1(
            value["client_mode"]
        )
    )
    if "destination_config" in value:
        import capo_iotsecuretunneling.types.destination_config

        out["destinationConfig"] = (
            capo_iotsecuretunneling.types.destination_config.serialize_aws_json_1_1(
                value["destination_config"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateTunnelAccessTokenRequest:
    out: RotateTunnelAccessTokenRequest = {}  # type: ignore[typeddict-item]
    if "clientMode" in data:
        import capo_iotsecuretunneling.types.client_mode

        out["client_mode"] = (
            capo_iotsecuretunneling.types.client_mode.deserialize_aws_json_1_1(
                data["clientMode"]
            )
        )
    else:
        raise DeserializationError(
            "RotateTunnelAccessTokenRequest.client_mode required"
        )
    if "destinationConfig" in data:
        import capo_iotsecuretunneling.types.destination_config

        out["destination_config"] = (
            capo_iotsecuretunneling.types.destination_config.deserialize_aws_json_1_1(
                data["destinationConfig"]
            )
        )
    return out
