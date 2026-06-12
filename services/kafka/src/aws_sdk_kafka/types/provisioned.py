"""Generated from Smithy shape ``com.amazonaws.kafka#Provisioned``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer_min1_max15
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.broker_node_group_info
    import aws_sdk_kafka.types.broker_software_info
    import aws_sdk_kafka.types.client_authentication
    import aws_sdk_kafka.types.customer_action_status
    import aws_sdk_kafka.types.encryption_info
    import aws_sdk_kafka.types.enhanced_monitoring
    import aws_sdk_kafka.types.logging_info
    import aws_sdk_kafka.types.open_monitoring_info
    import aws_sdk_kafka.types.rebalancing
    import aws_sdk_kafka.types.storage_mode


class Provisioned(TypedDict):
    broker_node_group_info: NotRequired[
        "aws_sdk_kafka.types.broker_node_group_info.BrokerNodeGroupInfo"
    ]
    """<p>Information about the brokers.</p>"""
    rebalancing: NotRequired["aws_sdk_kafka.types.rebalancing.Rebalancing"]
    """<p>Specifies whether or not intelligent rebalancing is turned on for a newly created MSK Provisioned cluster with Express brokers. Intelligent rebalancing performs automatic partition balancing operations when you scale your clusters up or down. By default, intelligent rebalancing is ACTIVE for all new Express-based clusters.</p>"""
    current_broker_software_info: NotRequired[
        "aws_sdk_kafka.types.broker_software_info.BrokerSoftwareInfo"
    ]
    """<p>Information about the Apache Kafka version deployed on the brokers.</p>"""
    client_authentication: NotRequired[
        "aws_sdk_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication information.</p>"""
    encryption_info: NotRequired["aws_sdk_kafka.types.encryption_info.EncryptionInfo"]
    """<p>Includes all encryption-related information.</p>"""
    enhanced_monitoring: NotRequired[
        "aws_sdk_kafka.types.enhanced_monitoring.EnhancedMonitoring"
    ]
    """<p>Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION.</p>"""
    open_monitoring: NotRequired[
        "aws_sdk_kafka.types.open_monitoring_info.OpenMonitoringInfo"
    ]
    """<p>The settings for open monitoring.</p>"""
    logging_info: NotRequired["aws_sdk_kafka.types.logging_info.LoggingInfo"]
    """<p>Log delivery information for the cluster.</p>"""
    number_of_broker_nodes: NotRequired[
        "aws_sdk_kafka.types.__integer_min1_max15.__integerMin1Max15"
    ]
    """<p>The number of broker nodes in the cluster.</p>"""
    zookeeper_connect_string: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The connection string to use to connect to the Apache ZooKeeper cluster.</p>"""
    zookeeper_connect_string_tls: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The connection string to use to connect to the Apache ZooKeeper cluster on a TLS port.</p>"""
    storage_mode: NotRequired["aws_sdk_kafka.types.storage_mode.StorageMode"]
    """<p>This controls storage mode for supported storage tiers.</p>"""
    customer_action_status: NotRequired[
        "aws_sdk_kafka.types.customer_action_status.CustomerActionStatus"
    ]
    """<p>Determines if there is an action required from the customer.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Provisioned) -> dict:
    out: dict = {}
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
    if "current_broker_software_info" in value:
        import aws_sdk_kafka.types.broker_software_info

        out["currentBrokerSoftwareInfo"] = (
            aws_sdk_kafka.types.broker_software_info.serialize_json(
                value["current_broker_software_info"]
            )
        )
    if "client_authentication" in value:
        import aws_sdk_kafka.types.client_authentication

        out["clientAuthentication"] = (
            aws_sdk_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
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
        import aws_sdk_kafka.types.open_monitoring_info

        out["openMonitoring"] = aws_sdk_kafka.types.open_monitoring_info.serialize_json(
            value["open_monitoring"]
        )
    if "logging_info" in value:
        import aws_sdk_kafka.types.logging_info

        out["loggingInfo"] = aws_sdk_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    if "number_of_broker_nodes" in value:
        out["numberOfBrokerNodes"] = value["number_of_broker_nodes"]
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


def deserialize_json(data: dict) -> Provisioned:
    out: Provisioned = {}  # type: ignore[typeddict-item]
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
    if "currentBrokerSoftwareInfo" in data:
        import aws_sdk_kafka.types.broker_software_info

        out["current_broker_software_info"] = (
            aws_sdk_kafka.types.broker_software_info.deserialize_json(
                data["currentBrokerSoftwareInfo"]
            )
        )
    if "clientAuthentication" in data:
        import aws_sdk_kafka.types.client_authentication

        out["client_authentication"] = (
            aws_sdk_kafka.types.client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
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
        import aws_sdk_kafka.types.open_monitoring_info

        out["open_monitoring"] = (
            aws_sdk_kafka.types.open_monitoring_info.deserialize_json(
                data["openMonitoring"]
            )
        )
    if "loggingInfo" in data:
        import aws_sdk_kafka.types.logging_info

        out["logging_info"] = aws_sdk_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if "numberOfBrokerNodes" in data:
        out["number_of_broker_nodes"] = data["numberOfBrokerNodes"]
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
