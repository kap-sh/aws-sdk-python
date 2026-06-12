"""Generated from Smithy shape ``com.amazonaws.transfer#SftpConnectorConnectionDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_transfer.types.sftp_connector_host_key


class SftpConnectorConnectionDetails(TypedDict):
    host_key: NotRequired[
        "aws_sdk_transfer.types.sftp_connector_host_key.SftpConnectorHostKey"
    ]
    """<p>The SSH public key of the remote SFTP server. This is returned during the initial connection attempt when you call <code>TestConnection</code>. It allows you to retrieve the valid server host key to update the connector when you are unable to obtain it in advance.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SftpConnectorConnectionDetails) -> dict:
    out: dict = {}
    if "host_key" in value:
        out["HostKey"] = value["host_key"]
    return out


def deserialize_aws_json_1_1(data: dict) -> SftpConnectorConnectionDetails:
    out: SftpConnectorConnectionDetails = {}  # type: ignore[typeddict-item]
    if "HostKey" in data:
        out["host_key"] = data["HostKey"]
    return out
