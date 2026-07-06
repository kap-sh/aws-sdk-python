"""Generated from Smithy shape ``com.amazonaws.iotsecuretunneling#RotateTunnelAccessTokenResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_iotsecuretunneling.types.client_access_token
    import aws_sdk_iotsecuretunneling.types.tunnel_arn


class RotateTunnelAccessTokenResponse(TypedDict, closed=True):
    tunnel_arn: NotRequired["aws_sdk_iotsecuretunneling.types.tunnel_arn.TunnelArn"]
    """<p>The Amazon Resource Name for the tunnel.</p>"""
    source_access_token: NotRequired[
        "aws_sdk_iotsecuretunneling.types.client_access_token.ClientAccessToken"
    ]
    """<p>The client access token that the source local proxy uses to connect to IoT Secure Tunneling.</p>"""
    destination_access_token: NotRequired[
        "aws_sdk_iotsecuretunneling.types.client_access_token.ClientAccessToken"
    ]
    """<p>The client access token that the destination local proxy uses to connect to IoT Secure Tunneling.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RotateTunnelAccessTokenResponse) -> dict:
    out: dict = {}
    if "tunnel_arn" in value:
        out["tunnelArn"] = value["tunnel_arn"]
    if "source_access_token" in value:
        out["sourceAccessToken"] = value["source_access_token"]
    if "destination_access_token" in value:
        out["destinationAccessToken"] = value["destination_access_token"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RotateTunnelAccessTokenResponse:
    out: RotateTunnelAccessTokenResponse = {}  # type: ignore[typeddict-item]
    if "tunnelArn" in data:
        out["tunnel_arn"] = data["tunnelArn"]
    if "sourceAccessToken" in data:
        out["source_access_token"] = data["sourceAccessToken"]
    if "destinationAccessToken" in data:
        out["destination_access_token"] = data["destinationAccessToken"]
    return out
