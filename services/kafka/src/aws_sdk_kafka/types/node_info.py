"""Generated from Smithy shape ``com.amazonaws.kafka#NodeInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.broker_node_info
    import aws_sdk_kafka.types.controller_node_info
    import aws_sdk_kafka.types.node_type
    import aws_sdk_kafka.types.zookeeper_node_info


class NodeInfo(TypedDict, closed=True):
    added_to_cluster_time: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The start time.</p>"""
    broker_node_info: NotRequired["aws_sdk_kafka.types.broker_node_info.BrokerNodeInfo"]
    """<p>The broker node info.</p>"""
    controller_node_info: NotRequired[
        "aws_sdk_kafka.types.controller_node_info.ControllerNodeInfo"
    ]
    """<p>The ControllerNodeInfo.</p>"""
    instance_type: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The instance type.</p>"""
    node_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the node.</p>"""
    node_type: NotRequired["aws_sdk_kafka.types.node_type.NodeType"]
    """<p>The node type.</p>"""
    zookeeper_node_info: NotRequired[
        "aws_sdk_kafka.types.zookeeper_node_info.ZookeeperNodeInfo"
    ]
    """<p>The ZookeeperNodeInfo.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: NodeInfo) -> dict:
    out: dict = {}
    if "added_to_cluster_time" in value:
        out["addedToClusterTime"] = value["added_to_cluster_time"]
    if "broker_node_info" in value:
        import aws_sdk_kafka.types.broker_node_info

        out["brokerNodeInfo"] = aws_sdk_kafka.types.broker_node_info.serialize_json(
            value["broker_node_info"]
        )
    if "controller_node_info" in value:
        import aws_sdk_kafka.types.controller_node_info

        out["controllerNodeInfo"] = (
            aws_sdk_kafka.types.controller_node_info.serialize_json(
                value["controller_node_info"]
            )
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "node_arn" in value:
        out["nodeARN"] = value["node_arn"]
    if "node_type" in value:
        import aws_sdk_kafka.types.node_type

        out["nodeType"] = aws_sdk_kafka.types.node_type.serialize_json(
            value["node_type"]
        )
    if "zookeeper_node_info" in value:
        import aws_sdk_kafka.types.zookeeper_node_info

        out["zookeeperNodeInfo"] = (
            aws_sdk_kafka.types.zookeeper_node_info.serialize_json(
                value["zookeeper_node_info"]
            )
        )
    return out


def deserialize_json(data: dict) -> NodeInfo:
    out: NodeInfo = {}  # type: ignore[typeddict-item]
    if "addedToClusterTime" in data:
        out["added_to_cluster_time"] = data["addedToClusterTime"]
    if "brokerNodeInfo" in data:
        import aws_sdk_kafka.types.broker_node_info

        out["broker_node_info"] = aws_sdk_kafka.types.broker_node_info.deserialize_json(
            data["brokerNodeInfo"]
        )
    if "controllerNodeInfo" in data:
        import aws_sdk_kafka.types.controller_node_info

        out["controller_node_info"] = (
            aws_sdk_kafka.types.controller_node_info.deserialize_json(
                data["controllerNodeInfo"]
            )
        )
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "nodeARN" in data:
        out["node_arn"] = data["nodeARN"]
    if "nodeType" in data:
        import aws_sdk_kafka.types.node_type

        out["node_type"] = aws_sdk_kafka.types.node_type.deserialize_json(
            data["nodeType"]
        )
    if "zookeeperNodeInfo" in data:
        import aws_sdk_kafka.types.zookeeper_node_info

        out["zookeeper_node_info"] = (
            aws_sdk_kafka.types.zookeeper_node_info.deserialize_json(
                data["zookeeperNodeInfo"]
            )
        )
    return out
