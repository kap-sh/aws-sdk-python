"""Generated from Smithy shape ``com.amazonaws.kafka#CreateClusterRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer_min1_max15
    import capo_kafka.types.__map_of__string
    import capo_kafka.types.__string_min1_max64
    import capo_kafka.types.__string_min1_max128
    import capo_kafka.types.broker_node_group_info
    import capo_kafka.types.client_authentication
    import capo_kafka.types.configuration_info
    import capo_kafka.types.encryption_info
    import capo_kafka.types.enhanced_monitoring
    import capo_kafka.types.logging_info
    import capo_kafka.types.open_monitoring_info
    import capo_kafka.types.rebalancing
    import capo_kafka.types.storage_mode


class CreateClusterRequest(TypedDict, closed=True):
    broker_node_group_info: NotRequired[
        "capo_kafka.types.broker_node_group_info.BrokerNodeGroupInfo"
    ]
    """<p>Information about the broker nodes in the cluster.</p>"""
    rebalancing: NotRequired["capo_kafka.types.rebalancing.Rebalancing"]
    """<p>Specifies if intelligent rebalancing should be turned on for the new MSK Provisioned cluster with Express brokers. By default, intelligent rebalancing status is ACTIVE for all new clusters.</p>"""
    client_authentication: NotRequired[
        "capo_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication related information.</p>"""
    cluster_name: NotRequired["capo_kafka.types.__string_min1_max64.__stringMin1Max64"]
    """<p>The name of the cluster.</p>"""
    configuration_info: NotRequired[
        "capo_kafka.types.configuration_info.ConfigurationInfo"
    ]
    """<p>Represents the configuration that you want MSK to use for the brokers in a cluster.</p>"""
    encryption_info: NotRequired["capo_kafka.types.encryption_info.EncryptionInfo"]
    """<p>Includes all encryption-related information.</p>"""
    enhanced_monitoring: NotRequired[
        "capo_kafka.types.enhanced_monitoring.EnhancedMonitoring"
    ]
    """<p>Specifies the level of monitoring for the MSK cluster. The possible values are DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION.</p>"""
    open_monitoring: NotRequired[
        "capo_kafka.types.open_monitoring_info.OpenMonitoringInfo"
    ]
    """<p>The settings for open monitoring.</p>"""
    kafka_version: NotRequired[
        "capo_kafka.types.__string_min1_max128.__stringMin1Max128"
    ]
    """<p>The version of Apache Kafka.</p>"""
    logging_info: NotRequired["capo_kafka.types.logging_info.LoggingInfo"]
    number_of_broker_nodes: NotRequired[
        "capo_kafka.types.__integer_min1_max15.__integerMin1Max15"
    ]
    """<p>The number of broker nodes in the cluster.</p>"""
    tags: NotRequired["capo_kafka.types.__map_of__string.__mapOf__string"]
    """<p>Create tags when creating the cluster.</p>"""
    storage_mode: NotRequired["capo_kafka.types.storage_mode.StorageMode"]
    """<p>This controls storage mode for supported storage tiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateClusterRequest) -> dict:
    out: dict = {}
    if "broker_node_group_info" in value:
        import capo_kafka.types.broker_node_group_info

        out["brokerNodeGroupInfo"] = (
            capo_kafka.types.broker_node_group_info.serialize_json(
                value["broker_node_group_info"]
            )
        )
    if "rebalancing" in value:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.serialize_json(
            value["rebalancing"]
        )
    if "client_authentication" in value:
        import capo_kafka.types.client_authentication

        out["clientAuthentication"] = (
            capo_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "cluster_name" in value:
        out["clusterName"] = value["cluster_name"]
    if "configuration_info" in value:
        import capo_kafka.types.configuration_info

        out["configurationInfo"] = capo_kafka.types.configuration_info.serialize_json(
            value["configuration_info"]
        )
    if "encryption_info" in value:
        import capo_kafka.types.encryption_info

        out["encryptionInfo"] = capo_kafka.types.encryption_info.serialize_json(
            value["encryption_info"]
        )
    if "enhanced_monitoring" in value:
        import capo_kafka.types.enhanced_monitoring

        out["enhancedMonitoring"] = capo_kafka.types.enhanced_monitoring.serialize_json(
            value["enhanced_monitoring"]
        )
    if "open_monitoring" in value:
        import capo_kafka.types.open_monitoring_info

        out["openMonitoring"] = capo_kafka.types.open_monitoring_info.serialize_json(
            value["open_monitoring"]
        )
    if "kafka_version" in value:
        out["kafkaVersion"] = value["kafka_version"]
    if "logging_info" in value:
        import capo_kafka.types.logging_info

        out["loggingInfo"] = capo_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    if "number_of_broker_nodes" in value:
        out["numberOfBrokerNodes"] = value["number_of_broker_nodes"]
    if "tags" in value:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.serialize_json(value["tags"])
    if "storage_mode" in value:
        import capo_kafka.types.storage_mode

        out["storageMode"] = capo_kafka.types.storage_mode.serialize_json(
            value["storage_mode"]
        )
    return out


def deserialize_json(data: dict) -> CreateClusterRequest:
    out: CreateClusterRequest = {}  # type: ignore[typeddict-item]
    if "brokerNodeGroupInfo" in data:
        import capo_kafka.types.broker_node_group_info

        out["broker_node_group_info"] = (
            capo_kafka.types.broker_node_group_info.deserialize_json(
                data["brokerNodeGroupInfo"]
            )
        )
    if "rebalancing" in data:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.deserialize_json(
            data["rebalancing"]
        )
    if "clientAuthentication" in data:
        import capo_kafka.types.client_authentication

        out["client_authentication"] = (
            capo_kafka.types.client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if "clusterName" in data:
        out["cluster_name"] = data["clusterName"]
    if "configurationInfo" in data:
        import capo_kafka.types.configuration_info

        out["configuration_info"] = (
            capo_kafka.types.configuration_info.deserialize_json(
                data["configurationInfo"]
            )
        )
    if "encryptionInfo" in data:
        import capo_kafka.types.encryption_info

        out["encryption_info"] = capo_kafka.types.encryption_info.deserialize_json(
            data["encryptionInfo"]
        )
    if "enhancedMonitoring" in data:
        import capo_kafka.types.enhanced_monitoring

        out["enhanced_monitoring"] = (
            capo_kafka.types.enhanced_monitoring.deserialize_json(
                data["enhancedMonitoring"]
            )
        )
    if "openMonitoring" in data:
        import capo_kafka.types.open_monitoring_info

        out["open_monitoring"] = capo_kafka.types.open_monitoring_info.deserialize_json(
            data["openMonitoring"]
        )
    if "kafkaVersion" in data:
        out["kafka_version"] = data["kafkaVersion"]
    if "loggingInfo" in data:
        import capo_kafka.types.logging_info

        out["logging_info"] = capo_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if "numberOfBrokerNodes" in data:
        out["number_of_broker_nodes"] = data["numberOfBrokerNodes"]
    if "tags" in data:
        import capo_kafka.types.__map_of__string

        out["tags"] = capo_kafka.types.__map_of__string.deserialize_json(data["tags"])
    if "storageMode" in data:
        import capo_kafka.types.storage_mode

        out["storage_mode"] = capo_kafka.types.storage_mode.deserialize_json(
            data["storageMode"]
        )
    return out
