"""Generated from Smithy shape ``com.amazonaws.kafka#ClusterInfo``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer
    import aws_sdk_kafka.types.__map_of__string
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.__timestamp_iso8601
    import aws_sdk_kafka.types.broker_node_group_info
    import aws_sdk_kafka.types.broker_software_info
    import aws_sdk_kafka.types.client_authentication
    import aws_sdk_kafka.types.cluster_state
    import aws_sdk_kafka.types.customer_action_status
    import aws_sdk_kafka.types.encryption_info
    import aws_sdk_kafka.types.enhanced_monitoring
    import aws_sdk_kafka.types.logging_info
    import aws_sdk_kafka.types.open_monitoring
    import aws_sdk_kafka.types.rebalancing
    import aws_sdk_kafka.types.state_info
    import aws_sdk_kafka.types.storage_mode


class ClusterInfo(TypedDict):
    active_operation_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>Arn of active cluster operation.</p>"""
    broker_node_group_info: NotRequired[
        "aws_sdk_kafka.types.broker_node_group_info.BrokerNodeGroupInfo"
    ]
    """<p>Information about the broker nodes.</p>"""
    rebalancing: NotRequired["aws_sdk_kafka.types.rebalancing.Rebalancing"]
    """<p>Contains information about intelligent rebalancing for new MSK Provisioned clusters with Express brokers. By default, intelligent rebalancing status is ACTIVE.</p>"""
    client_authentication: NotRequired[
        "aws_sdk_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication information.</p>"""
    cluster_arn: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) that uniquely identifies the cluster.</p>"""
    cluster_name: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The name of the cluster.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafka.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time when the cluster was created.</p>"""
    current_broker_software_info: NotRequired[
        "aws_sdk_kafka.types.broker_software_info.BrokerSoftwareInfo"
    ]
    """<p>Information about the version of software currently deployed on the Apache Kafka brokers in the cluster.</p>"""
    current_version: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The current version of the MSK cluster.</p>"""
    encryption_info: NotRequired["aws_sdk_kafka.types.encryption_info.EncryptionInfo"]
    """<p>Includes all encryption-related information.</p>"""
    enhanced_monitoring: NotRequired[
        "aws_sdk_kafka.types.enhanced_monitoring.EnhancedMonitoring"
    ]
    """<p>Specifies which metrics are gathered for the MSK cluster. This property has the following possible values: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. For a list of the metrics associated with each of these levels of monitoring, see <a href=\"https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html\">Monitoring</a>.</p>"""
    open_monitoring: NotRequired["aws_sdk_kafka.types.open_monitoring.OpenMonitoring"]
    """<p>Settings for open monitoring using Prometheus.</p>"""
    logging_info: NotRequired["aws_sdk_kafka.types.logging_info.LoggingInfo"]
    number_of_broker_nodes: NotRequired["aws_sdk_kafka.types.__integer.__integer"]
    """<p>The number of broker nodes in the cluster.</p>"""
    state: NotRequired["aws_sdk_kafka.types.cluster_state.ClusterState"]
    """<p>The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING.</p>"""
    state_info: NotRequired["aws_sdk_kafka.types.state_info.StateInfo"]
    tags: NotRequired["aws_sdk_kafka.types.__map_of__string.__mapOf__string"]
    """<p>Tags attached to the cluster.</p>"""
    zookeeper_connect_string: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The connection string to use to connect to the Apache ZooKeeper cluster.</p>"""
    zookeeper_connect_string_tls: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The connection string to use to connect to zookeeper cluster on Tls port.</p>"""
    storage_mode: NotRequired["aws_sdk_kafka.types.storage_mode.StorageMode"]
    """<p>This controls storage mode for supported storage tiers.</p>"""
    customer_action_status: NotRequired[
        "aws_sdk_kafka.types.customer_action_status.CustomerActionStatus"
    ]
    """<p>Determines if there is an action required from the customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ClusterInfo) -> dict:
    out: dict = {}
    if "active_operation_arn" in value:
        out["activeOperationArn"] = value["active_operation_arn"]
    if "broker_node_group_info" in value:
        import aws_sdk_kafka.types.broker_node_group_info

        out["brokerNodeGroupInfo"] = (
            aws_sdk_kafka.types.broker_node_group_info.serialize_json(
                value["broker_node_group_info"]
            )
        )
    if "rebalancing" in value:
        import aws_sdk_kafka.types.rebalancing

        out["rebalancing"] = aws_sdk_kafka.types.rebalancing.serialize_json(
            value["rebalancing"]
        )
    if "client_authentication" in value:
        import aws_sdk_kafka.types.client_authentication

        out["clientAuthentication"] = (
            aws_sdk_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "cluster_arn" in value:
        out["clusterArn"] = value["cluster_arn"]
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "creation_time" in value:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creationTime"] = aws_sdk_kafka.types.__timestamp_iso8601.serialize_json(
            value["creation_time"]
        )
    if "current_broker_software_info" in value:
        import aws_sdk_kafka.types.broker_software_info

        out["currentBrokerSoftwareInfo"] = (
            aws_sdk_kafka.types.broker_software_info.serialize_json(
                value["current_broker_software_info"]
            )
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "encryption_info" in value:
        import aws_sdk_kafka.types.encryption_info

        out["encryptionInfo"] = aws_sdk_kafka.types.encryption_info.serialize_json(
            value["encryption_info"]
        )
    if "enhanced_monitoring" in value:
        import aws_sdk_kafka.types.enhanced_monitoring

        out["enhancedMonitoring"] = (
            aws_sdk_kafka.types.enhanced_monitoring.serialize_json(
                value["enhanced_monitoring"]
            )
        )
    if "open_monitoring" in value:
        import aws_sdk_kafka.types.open_monitoring

        out["openMonitoring"] = aws_sdk_kafka.types.open_monitoring.serialize_json(
            value["open_monitoring"]
        )
    if "logging_info" in value:
        import aws_sdk_kafka.types.logging_info

        out["loggingInfo"] = aws_sdk_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    if "number_of_broker_nodes" in value:
        out["numberOfBrokerNodes"] = value["number_of_broker_nodes"]
    if "state" in value:
        import aws_sdk_kafka.types.cluster_state

        out["state"] = aws_sdk_kafka.types.cluster_state.serialize_json(value["state"])
    if "state_info" in value:
        import aws_sdk_kafka.types.state_info

        out["stateInfo"] = aws_sdk_kafka.types.state_info.serialize_json(
            value["state_info"]
        )
    if "tags" in value:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "zookeeper_connect_string" in value:
        out["zookeeperConnectString"] = value["zookeeper_connect_string"]
    if "zookeeper_connect_string_tls" in value:
        out["zookeeperConnectStringTls"] = value["zookeeper_connect_string_tls"]
    if "storage_mode" in value:
        import aws_sdk_kafka.types.storage_mode

        out["storageMode"] = aws_sdk_kafka.types.storage_mode.serialize_json(
            value["storage_mode"]
        )
    if "customer_action_status" in value:
        import aws_sdk_kafka.types.customer_action_status

        out["customerActionStatus"] = (
            aws_sdk_kafka.types.customer_action_status.serialize_json(
                value["customer_action_status"]
            )
        )
    return out


def deserialize_json(data: dict) -> ClusterInfo:
    out: ClusterInfo = {}  # type: ignore[typeddict-item]
    if "activeOperationArn" in data:
        out["active_operation_arn"] = data["activeOperationArn"]
    if "brokerNodeGroupInfo" in data:
        import aws_sdk_kafka.types.broker_node_group_info

        out["broker_node_group_info"] = (
            aws_sdk_kafka.types.broker_node_group_info.deserialize_json(
                data["brokerNodeGroupInfo"]
            )
        )
    if "rebalancing" in data:
        import aws_sdk_kafka.types.rebalancing

        out["rebalancing"] = aws_sdk_kafka.types.rebalancing.deserialize_json(
            data["rebalancing"]
        )
    if "clientAuthentication" in data:
        import aws_sdk_kafka.types.client_authentication

        out["client_authentication"] = (
            aws_sdk_kafka.types.client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if "clusterArn" in data:
        out["cluster_arn"] = data["clusterArn"]
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "creationTime" in data:
        import aws_sdk_kafka.types.__timestamp_iso8601

        out["creation_time"] = aws_sdk_kafka.types.__timestamp_iso8601.deserialize_json(
            data["creationTime"]
        )
    if "currentBrokerSoftwareInfo" in data:
        import aws_sdk_kafka.types.broker_software_info

        out["current_broker_software_info"] = (
            aws_sdk_kafka.types.broker_software_info.deserialize_json(
                data["currentBrokerSoftwareInfo"]
            )
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "encryptionInfo" in data:
        import aws_sdk_kafka.types.encryption_info

        out["encryption_info"] = aws_sdk_kafka.types.encryption_info.deserialize_json(
            data["encryptionInfo"]
        )
    if "enhancedMonitoring" in data:
        import aws_sdk_kafka.types.enhanced_monitoring

        out["enhanced_monitoring"] = (
            aws_sdk_kafka.types.enhanced_monitoring.deserialize_json(
                data["enhancedMonitoring"]
            )
        )
    if "openMonitoring" in data:
        import aws_sdk_kafka.types.open_monitoring

        out["open_monitoring"] = aws_sdk_kafka.types.open_monitoring.deserialize_json(
            data["openMonitoring"]
        )
    if "loggingInfo" in data:
        import aws_sdk_kafka.types.logging_info

        out["logging_info"] = aws_sdk_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if "numberOfBrokerNodes" in data:
        out["number_of_broker_nodes"] = data["numberOfBrokerNodes"]
    if "state" in data:
        import aws_sdk_kafka.types.cluster_state

        out["state"] = aws_sdk_kafka.types.cluster_state.deserialize_json(data["state"])
    if "stateInfo" in data:
        import aws_sdk_kafka.types.state_info

        out["state_info"] = aws_sdk_kafka.types.state_info.deserialize_json(
            data["stateInfo"]
        )
    if "tags" in data:
        import aws_sdk_kafka.types.__map_of__string

        out["tags"] = aws_sdk_kafka.types.__map_of__string.deserialize_json(
            data["tags"]
        )
    if "zookeeperConnectString" in data:
        out["zookeeper_connect_string"] = data["zookeeperConnectString"]
    if "zookeeperConnectStringTls" in data:
        out["zookeeper_connect_string_tls"] = data["zookeeperConnectStringTls"]
    if "storageMode" in data:
        import aws_sdk_kafka.types.storage_mode

        out["storage_mode"] = aws_sdk_kafka.types.storage_mode.deserialize_json(
            data["storageMode"]
        )
    if "customerActionStatus" in data:
        import aws_sdk_kafka.types.customer_action_status

        out["customer_action_status"] = (
            aws_sdk_kafka.types.customer_action_status.deserialize_json(
                data["customerActionStatus"]
            )
        )
    return out
