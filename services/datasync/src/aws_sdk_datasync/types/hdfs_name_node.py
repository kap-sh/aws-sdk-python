"""Generated from Smithy shape ``com.amazonaws.datasync#HdfsNameNode``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_datasync.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_datasync.types.hdfs_server_hostname
    import aws_sdk_datasync.types.hdfs_server_port


class HdfsNameNode(TypedDict):
    hostname: "aws_sdk_datasync.types.hdfs_server_hostname.HdfsServerHostname"
    """<p>The hostname of the NameNode in the HDFS cluster. This value is the IP address or Domain Name Service (DNS) name of the NameNode. An agent that's installed on-premises uses this hostname to communicate with the NameNode in the network.</p>"""
    port: "aws_sdk_datasync.types.hdfs_server_port.HdfsServerPort"
    """<p>The port that the NameNode uses to listen to client requests.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: HdfsNameNode) -> dict:
    out: dict = {}
    out["Hostname"] = value["hostname"]
    out["Port"] = value["port"]
    return out


def deserialize_aws_json_1_1(data: dict) -> HdfsNameNode:
    out: HdfsNameNode = {}  # type: ignore[typeddict-item]
    if "Hostname" in data:
        out["hostname"] = data["Hostname"]
    else:
        raise DeserializationError("HdfsNameNode.hostname required")
    if "Port" in data:
        out["port"] = data["Port"]
    else:
        raise DeserializationError("HdfsNameNode.port required")
    return out
