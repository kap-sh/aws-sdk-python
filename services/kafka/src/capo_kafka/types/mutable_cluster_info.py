"""Generated from Smithy shape ``com.amazonaws.kafka#MutableClusterInfo``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kafka.types.__integer
    import capo_kafka.types.__list_of_broker_ebs_volume_info
    import capo_kafka.types.__string
    import capo_kafka.types.__string_min5_max32
    import capo_kafka.types.broker_count_update_info
    import capo_kafka.types.client_authentication
    import capo_kafka.types.configuration_info
    import capo_kafka.types.connectivity_info
    import capo_kafka.types.encryption_info
    import capo_kafka.types.enhanced_monitoring
    import capo_kafka.types.logging_info
    import capo_kafka.types.open_monitoring
    import capo_kafka.types.rebalancing
    import capo_kafka.types.storage_mode
    import capo_kafka.types.zookeeper_access


class MutableClusterInfo(TypedDict, closed=True):
    broker_ebs_volume_info: NotRequired[
        "capo_kafka.types.__list_of_broker_ebs_volume_info.__listOfBrokerEBSVolumeInfo"
    ]
    """<p>Specifies the size of the EBS volume and the ID of the associated broker.</p>"""
    configuration_info: NotRequired[
        "capo_kafka.types.configuration_info.ConfigurationInfo"
    ]
    """<p>Information about the changes in the configuration of the brokers.</p>"""
    number_of_broker_nodes: NotRequired["capo_kafka.types.__integer.__integer"]
    """<p>The number of broker nodes in the cluster.</p>"""
    enhanced_monitoring: NotRequired[
        "capo_kafka.types.enhanced_monitoring.EnhancedMonitoring"
    ]
    """<p>Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.</p>"""
    open_monitoring: NotRequired["capo_kafka.types.open_monitoring.OpenMonitoring"]
    """<p>The settings for open monitoring.</p>"""
    zookeeper_access: NotRequired["capo_kafka.types.zookeeper_access.ZookeeperAccess"]
    """<p>Access control settings for zookeeper</p>"""
    kafka_version: NotRequired["capo_kafka.types.__string.__string"]
    """<p>The Apache Kafka version.</p>"""
    logging_info: NotRequired["capo_kafka.types.logging_info.LoggingInfo"]
    """<p>You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.</p>"""
    instance_type: NotRequired["capo_kafka.types.__string_min5_max32.__stringMin5Max32"]
    """<p>Information about the Amazon MSK broker type.</p>"""
    client_authentication: NotRequired[
        "capo_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication information.</p>"""
    encryption_info: NotRequired["capo_kafka.types.encryption_info.EncryptionInfo"]
    """<p>Includes all encryption-related information.</p>"""
    connectivity_info: NotRequired[
        "capo_kafka.types.connectivity_info.ConnectivityInfo"
    ]
    """<p>Information about the broker access configuration.</p>"""
    storage_mode: NotRequired["capo_kafka.types.storage_mode.StorageMode"]
    """<p>This controls storage mode for supported storage tiers.</p>"""
    broker_count_update_info: NotRequired[
        "capo_kafka.types.broker_count_update_info.BrokerCountUpdateInfo"
    ]
    """<p>Describes brokers being changed during a broker count update.</p>"""
    rebalancing: NotRequired["capo_kafka.types.rebalancing.Rebalancing"]
    """<p>Describes the intelligent rebalancing configuration of an MSK Provisioned cluster with Express brokers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MutableClusterInfo) -> dict:
    out: dict = {}
    if "broker_ebs_volume_info" in value:
        import capo_kafka.types.__list_of_broker_ebs_volume_info

        out["brokerEBSVolumeInfo"] = (
            capo_kafka.types.__list_of_broker_ebs_volume_info.serialize_json(
                value["broker_ebs_volume_info"]
            )
        )
    if "configuration_info" in value:
        import capo_kafka.types.configuration_info

        out["configurationInfo"] = capo_kafka.types.configuration_info.serialize_json(
            value["configuration_info"]
        )
    if "number_of_broker_nodes" in value:
        out["numberOfBrokerNodes"] = value["number_of_broker_nodes"]
    if "enhanced_monitoring" in value:
        import capo_kafka.types.enhanced_monitoring

        out["enhancedMonitoring"] = capo_kafka.types.enhanced_monitoring.serialize_json(
            value["enhanced_monitoring"]
        )
    if "open_monitoring" in value:
        import capo_kafka.types.open_monitoring

        out["openMonitoring"] = capo_kafka.types.open_monitoring.serialize_json(
            value["open_monitoring"]
        )
    if "zookeeper_access" in value:
        import capo_kafka.types.zookeeper_access

        out["zookeeperAccess"] = capo_kafka.types.zookeeper_access.serialize_json(
            value["zookeeper_access"]
        )
    if "kafka_version" in value:
        out["kafkaVersion"] = value["kafka_version"]
    if "logging_info" in value:
        import capo_kafka.types.logging_info

        out["loggingInfo"] = capo_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    if "instance_type" in value:
        out["instanceType"] = value["instance_type"]
    if "client_authentication" in value:
        import capo_kafka.types.client_authentication

        out["clientAuthentication"] = (
            capo_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "encryption_info" in value:
        import capo_kafka.types.encryption_info

        out["encryptionInfo"] = capo_kafka.types.encryption_info.serialize_json(
            value["encryption_info"]
        )
    if "connectivity_info" in value:
        import capo_kafka.types.connectivity_info

        out["connectivityInfo"] = capo_kafka.types.connectivity_info.serialize_json(
            value["connectivity_info"]
        )
    if "storage_mode" in value:
        import capo_kafka.types.storage_mode

        out["storageMode"] = capo_kafka.types.storage_mode.serialize_json(
            value["storage_mode"]
        )
    if "broker_count_update_info" in value:
        import capo_kafka.types.broker_count_update_info

        out["brokerCountUpdateInfo"] = (
            capo_kafka.types.broker_count_update_info.serialize_json(
                value["broker_count_update_info"]
            )
        )
    if "rebalancing" in value:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.serialize_json(
            value["rebalancing"]
        )
    return out


def deserialize_json(data: dict) -> MutableClusterInfo:
    out: MutableClusterInfo = {}  # type: ignore[typeddict-item]
    if "brokerEBSVolumeInfo" in data:
        import capo_kafka.types.__list_of_broker_ebs_volume_info

        out["broker_ebs_volume_info"] = (
            capo_kafka.types.__list_of_broker_ebs_volume_info.deserialize_json(
                data["brokerEBSVolumeInfo"]
            )
        )
    if "configurationInfo" in data:
        import capo_kafka.types.configuration_info

        out["configuration_info"] = (
            capo_kafka.types.configuration_info.deserialize_json(
                data["configurationInfo"]
            )
        )
    if "numberOfBrokerNodes" in data:
        out["number_of_broker_nodes"] = data["numberOfBrokerNodes"]
    if "enhancedMonitoring" in data:
        import capo_kafka.types.enhanced_monitoring

        out["enhanced_monitoring"] = (
            capo_kafka.types.enhanced_monitoring.deserialize_json(
                data["enhancedMonitoring"]
            )
        )
    if "openMonitoring" in data:
        import capo_kafka.types.open_monitoring

        out["open_monitoring"] = capo_kafka.types.open_monitoring.deserialize_json(
            data["openMonitoring"]
        )
    if "zookeeperAccess" in data:
        import capo_kafka.types.zookeeper_access

        out["zookeeper_access"] = capo_kafka.types.zookeeper_access.deserialize_json(
            data["zookeeperAccess"]
        )
    if "kafkaVersion" in data:
        out["kafka_version"] = data["kafkaVersion"]
    if "loggingInfo" in data:
        import capo_kafka.types.logging_info

        out["logging_info"] = capo_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if "instanceType" in data:
        out["instance_type"] = data["instanceType"]
    if "clientAuthentication" in data:
        import capo_kafka.types.client_authentication

        out["client_authentication"] = (
            capo_kafka.types.client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if "encryptionInfo" in data:
        import capo_kafka.types.encryption_info

        out["encryption_info"] = capo_kafka.types.encryption_info.deserialize_json(
            data["encryptionInfo"]
        )
    if "connectivityInfo" in data:
        import capo_kafka.types.connectivity_info

        out["connectivity_info"] = capo_kafka.types.connectivity_info.deserialize_json(
            data["connectivityInfo"]
        )
    if "storageMode" in data:
        import capo_kafka.types.storage_mode

        out["storage_mode"] = capo_kafka.types.storage_mode.deserialize_json(
            data["storageMode"]
        )
    if "brokerCountUpdateInfo" in data:
        import capo_kafka.types.broker_count_update_info

        out["broker_count_update_info"] = (
            capo_kafka.types.broker_count_update_info.deserialize_json(
                data["brokerCountUpdateInfo"]
            )
        )
    if "rebalancing" in data:
        import capo_kafka.types.rebalancing

        out["rebalancing"] = capo_kafka.types.rebalancing.deserialize_json(
            data["rebalancing"]
        )
    return out
