"""Generated from Smithy shape ``com.amazonaws.mailmanager#UpdateRelayRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.relay_authentication
    import aws_sdk_mailmanager.types.relay_id
    import aws_sdk_mailmanager.types.relay_name
    import aws_sdk_mailmanager.types.relay_server_name
    import aws_sdk_mailmanager.types.relay_server_port


class UpdateRelayRequest(TypedDict, closed=True):
    relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId"
    """<p>The unique relay identifier.</p>"""
    relay_name: NotRequired["aws_sdk_mailmanager.types.relay_name.RelayName"]
    """<p>The name of the relay resource.</p>"""
    server_name: NotRequired[
        "aws_sdk_mailmanager.types.relay_server_name.RelayServerName"
    ]
    """<p>The destination relay server address.</p>"""
    server_port: NotRequired[
        "aws_sdk_mailmanager.types.relay_server_port.RelayServerPort"
    ]
    """<p>The destination relay server port.</p>"""
    authentication: NotRequired[
        "aws_sdk_mailmanager.types.relay_authentication.RelayAuthentication"
    ]
    """<p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateRelayRequest) -> dict:
    out: dict = {}
    out["RelayId"] = value["relay_id"]
    if "relay_name" in value:
        out["RelayName"] = value["relay_name"]
    if "server_name" in value:
        out["ServerName"] = value["server_name"]
    if "server_port" in value:
        out["ServerPort"] = value["server_port"]
    if "authentication" in value:
        import aws_sdk_mailmanager.types.relay_authentication

        out["Authentication"] = (
            aws_sdk_mailmanager.types.relay_authentication.serialize_aws_json_1_0(
                value["authentication"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateRelayRequest:
    out: UpdateRelayRequest = {}  # type: ignore[typeddict-item]
    if "RelayId" in data:
        out["relay_id"] = data["RelayId"]
    else:
        raise DeserializationError("UpdateRelayRequest.relay_id required")
    if "RelayName" in data:
        out["relay_name"] = data["RelayName"]
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    if "ServerPort" in data:
        out["server_port"] = data["ServerPort"]
    if "Authentication" in data:
        import aws_sdk_mailmanager.types.relay_authentication

        out["authentication"] = (
            aws_sdk_mailmanager.types.relay_authentication.deserialize_aws_json_1_0(
                data["Authentication"]
            )
        )
    return out
