"""Generated from Smithy shape ``com.amazonaws.mailmanager#CreateRelayRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_mailmanager.types.idempotency_token
    import aws_sdk_mailmanager.types.relay_authentication
    import aws_sdk_mailmanager.types.relay_name
    import aws_sdk_mailmanager.types.relay_server_name
    import aws_sdk_mailmanager.types.relay_server_port
    import aws_sdk_mailmanager.types.tag_list


class CreateRelayRequest(TypedDict):
    client_token: NotRequired[
        "aws_sdk_mailmanager.types.idempotency_token.IdempotencyToken"
    ]
    """<p>A unique token that Amazon SES uses to recognize subsequent retries of the same request.</p>"""
    relay_name: "aws_sdk_mailmanager.types.relay_name.RelayName"
    """<p>The unique name of the relay resource.</p>"""
    server_name: "aws_sdk_mailmanager.types.relay_server_name.RelayServerName"
    """<p>The destination relay server address.</p>"""
    server_port: "aws_sdk_mailmanager.types.relay_server_port.RelayServerPort"
    """<p>The destination relay server port.</p>"""
    authentication: "aws_sdk_mailmanager.types.relay_authentication.RelayAuthentication"
    """<p>Authentication for the relay destination server—specify the secretARN where the SMTP credentials are stored.</p>"""
    tags: NotRequired["aws_sdk_mailmanager.types.tag_list.TagList"]
    r"""<p>The tags used to organize, track, or control access for the resource. For example, { \"tags\": {\"key1\":\"value1\", \"key2\":\"value2\"} }.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateRelayRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    out["RelayName"] = value["relay_name"]
    out["ServerName"] = value["server_name"]
    out["ServerPort"] = value["server_port"]
    import aws_sdk_mailmanager.types.relay_authentication

    out["Authentication"] = (
        aws_sdk_mailmanager.types.relay_authentication.serialize_aws_json_1_0(
            value["authentication"]
        )
    )
    if "tags" in value:
        import aws_sdk_mailmanager.types.tag_list

        out["Tags"] = aws_sdk_mailmanager.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateRelayRequest:
    out: CreateRelayRequest = {}  # type: ignore[typeddict-item]
    if "ClientToken" in data:
        out["client_token"] = data["ClientToken"]
    if "RelayName" in data:
        out["relay_name"] = data["RelayName"]
    else:
        raise DeserializationError("CreateRelayRequest.relay_name required")
    if "ServerName" in data:
        out["server_name"] = data["ServerName"]
    else:
        raise DeserializationError("CreateRelayRequest.server_name required")
    if "ServerPort" in data:
        out["server_port"] = data["ServerPort"]
    else:
        raise DeserializationError("CreateRelayRequest.server_port required")
    if "Authentication" in data:
        import aws_sdk_mailmanager.types.relay_authentication

        out["authentication"] = (
            aws_sdk_mailmanager.types.relay_authentication.deserialize_aws_json_1_0(
                data["Authentication"]
            )
        )
    else:
        raise DeserializationError("CreateRelayRequest.authentication required")
    if "Tags" in data:
        import aws_sdk_mailmanager.types.tag_list

        out["tags"] = aws_sdk_mailmanager.types.tag_list.deserialize_aws_json_1_0(
            data["Tags"]
        )
    return out
