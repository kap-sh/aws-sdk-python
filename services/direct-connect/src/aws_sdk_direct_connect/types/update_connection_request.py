"""Generated from Smithy shape ``com.amazonaws.directconnect#UpdateConnectionRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_direct_connect.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_direct_connect.types.connection_id
    import aws_sdk_direct_connect.types.connection_name
    import aws_sdk_direct_connect.types.encryption_mode


class UpdateConnectionRequest(TypedDict):
    connection_id: "aws_sdk_direct_connect.types.connection_id.ConnectionId"
    """<p>The ID of the connection.</p> <p>You can use <a>DescribeConnections</a> to retrieve the connection ID.</p>"""
    connection_name: NotRequired[
        "aws_sdk_direct_connect.types.connection_name.ConnectionName"
    ]
    """<p>The name of the connection.</p>"""
    encryption_mode: NotRequired[
        "aws_sdk_direct_connect.types.encryption_mode.EncryptionMode"
    ]
    """<p>The connection MAC Security (MACsec) encryption mode.</p> <p>The valid values are <code>no_encrypt</code>, <code>should_encrypt</code>, and <code>must_encrypt</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateConnectionRequest) -> dict:
    out: dict = {}
    out["connectionId"] = value["connection_id"]
    if "connection_name" in value:
        out["connectionName"] = value["connection_name"]
    if "encryption_mode" in value:
        out["encryptionMode"] = value["encryption_mode"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateConnectionRequest:
    out: UpdateConnectionRequest = {}  # type: ignore[typeddict-item]
    if "connectionId" in data:
        out["connection_id"] = data["connectionId"]
    else:
        raise DeserializationError("UpdateConnectionRequest.connection_id required")
    if "connectionName" in data:
        out["connection_name"] = data["connectionName"]
    if "encryptionMode" in data:
        out["encryption_mode"] = data["encryptionMode"]
    return out
