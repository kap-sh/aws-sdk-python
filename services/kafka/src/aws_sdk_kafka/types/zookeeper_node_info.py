"""Generated from Smithy shape ``com.amazonaws.kafka#ZookeeperNodeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__double
    import aws_sdk_kafka.types.__list_of__string
    import aws_sdk_kafka.types.__string


class ZookeeperNodeInfo(TypedDict, closed=True):
    attached_eni_id: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The attached elastic network interface of the broker.</p>"""
    client_vpc_ip_address: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The virtual private cloud (VPC) IP address of the client.</p>"""
    endpoints: NotRequired["aws_sdk_kafka.types.__list_of__string.__listOf__string"]
    """<p>Endpoints for accessing the ZooKeeper.</p>"""
    zookeeper_id: NotRequired["aws_sdk_kafka.types.__double.__double"]
    """<p>The role-specific ID for Zookeeper.</p>"""
    zookeeper_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The version of Zookeeper.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ZookeeperNodeInfo) -> dict:
    out: dict = {}
    if "attached_eni_id" in value:
        out["attachedENIId"] = value["attached_eni_id"]
    if "client_vpc_ip_address" in value:
        out["clientVpcIpAddress"] = value["client_vpc_ip_address"]
    if "endpoints" in value:
        import aws_sdk_kafka.types.__list_of__string

        out["endpoints"] = aws_sdk_kafka.types.__list_of__string.serialize_json(
            value["endpoints"]
        )
    if "zookeeper_id" in value:
        out["zookeeperId"] = value["zookeeper_id"]
    if "zookeeper_version" in value:
        out["zookeeperVersion"] = value["zookeeper_version"]
    return out


def deserialize_json(data: dict) -> ZookeeperNodeInfo:
    out: ZookeeperNodeInfo = {}  # type: ignore[typeddict-item]
    if "attachedENIId" in data:
        out["attached_eni_id"] = data["attachedENIId"]
    if "clientVpcIpAddress" in data:
        out["client_vpc_ip_address"] = data["clientVpcIpAddress"]
    if "endpoints" in data:
        import aws_sdk_kafka.types.__list_of__string

        out["endpoints"] = aws_sdk_kafka.types.__list_of__string.deserialize_json(
            data["endpoints"]
        )
    if "zookeeperId" in data:
        out["zookeeper_id"] = data["zookeeperId"]
    if "zookeeperVersion" in data:
        out["zookeeper_version"] = data["zookeeperVersion"]
    return out
