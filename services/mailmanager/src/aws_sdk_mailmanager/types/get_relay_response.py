"""Generated from Smithy shape ``com.amazonaws.mailmanager#GetRelayResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_mailmanager.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import aws_sdk_mailmanager.types.relay_arn
    import aws_sdk_mailmanager.types.relay_authentication
    import aws_sdk_mailmanager.types.relay_id
    import aws_sdk_mailmanager.types.relay_name
    import aws_sdk_mailmanager.types.relay_server_name
    import aws_sdk_mailmanager.types.relay_server_port


class GetRelayResponse(TypedDict, closed=True):
    relay_id: "aws_sdk_mailmanager.types.relay_id.RelayId"
    """<p>The unique relay identifier.</p>"""
    relay_arn: NotRequired["aws_sdk_mailmanager.types.relay_arn.RelayArn"]
    """<p>The Amazon Resource Name (ARN) of the relay.</p>"""
    relay_name: NotRequired["aws_sdk_mailmanager.types.relay_name.RelayName"]
    """<p>The unique name of the relay.</p>"""
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
    """<p>The authentication attribute—contains the secret ARN where the customer relay server credentials are stored. </p>"""
    created_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when the relay was created.</p>"""
    last_modified_timestamp: NotRequired["datetime.datetime"]
    """<p>The timestamp of when relay was last updated.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetRelayResponse) -> dict:
    out: dict = {}
    out["RelayId"] = value["relay_id"]
    if "relay_arn" in value:
        out["RelayArn"] = value["relay_arn"]
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
    if "created_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["CreatedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["created_timestamp"]
            )
        )
    if "last_modified_timestamp" in value:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["LastModifiedTimestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_modified_timestamp"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetRelayResponse:
    out: GetRelayResponse = {}  # type: ignore[typeddict-item]
    if "RelayId" in data:
        out["relay_id"] = data["RelayId"]
    else:
        raise DeserializationError("GetRelayResponse.relay_id required")
    if "RelayArn" in data:
        out["relay_arn"] = data["RelayArn"]
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
    if "CreatedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["created_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["CreatedTimestamp"]
            )
        )
    if "LastModifiedTimestamp" in data:
        import aws_sdk_mailmanager.types._prelude.timestamp

        out["last_modified_timestamp"] = (
            aws_sdk_mailmanager.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["LastModifiedTimestamp"]
            )
        )
    return out
