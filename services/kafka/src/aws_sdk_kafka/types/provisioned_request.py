"""Generated from Smithy shape ``com.amazonaws.kafka#ProvisionedRequest``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__integer_min1_max15
    import aws_sdk_kafka.types.__string_min1_max128
    import aws_sdk_kafka.types.broker_node_group_info
    import aws_sdk_kafka.types.client_authentication
    import aws_sdk_kafka.types.configuration_info
    import aws_sdk_kafka.types.encryption_info
    import aws_sdk_kafka.types.enhanced_monitoring
    import aws_sdk_kafka.types.logging_info
    import aws_sdk_kafka.types.open_monitoring_info
    import aws_sdk_kafka.types.rebalancing
    import aws_sdk_kafka.types.storage_mode


class ProvisionedRequest(TypedDict):
    broker_node_group_info: NotRequired[
        "aws_sdk_kafka.types.broker_node_group_info.BrokerNodeGroupInfo"
    ]
    """<p>Information about the brokers.</p>"""
    rebalancing: NotRequired["aws_sdk_kafka.types.rebalancing.Rebalancing"]
    """<p>Specifies if intelligent rebalancing is turned on for your MSK Provisioned cluster with Express brokers. For all new Express-based clusters that you create, intelligent rebalancing is turned on by default.</p>"""
    client_authentication: NotRequired[
        "aws_sdk_kafka.types.client_authentication.ClientAuthentication"
    ]
    """<p>Includes all client authentication information.</p>"""
    configuration_info: NotRequired[
        "aws_sdk_kafka.types.configuration_info.ConfigurationInfo"
    ]
    """<p>Represents the configuration that you want Amazon MSK to use for the brokers in a cluster.</p>"""
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
    kafka_version: NotRequired[
        "aws_sdk_kafka.types.__string_min1_max128.__stringMin1Max128"
    ]
    """<p>The Apache Kafka version that you want for the cluster.</p>"""
    logging_info: NotRequired["aws_sdk_kafka.types.logging_info.LoggingInfo"]
    """<p>Log delivery information for the cluster.</p>"""
    number_of_broker_nodes: NotRequired[
        "aws_sdk_kafka.types.__integer_min1_max15.__integerMin1Max15"
    ]
    """<p>The number of broker nodes in the cluster.</p>"""
    storage_mode: NotRequired["aws_sdk_kafka.types.storage_mode.StorageMode"]
    """<p>This controls storage mode for supported storage tiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProvisionedRequest) -> dict:
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
    if "client_authentication" in value:
        import aws_sdk_kafka.types.client_authentication

        out["clientAuthentication"] = (
            aws_sdk_kafka.types.client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "configuration_info" in value:
        import aws_sdk_kafka.types.configuration_info

        out["configurationInfo"] = (
            aws_sdk_kafka.types.configuration_info.serialize_json(
                value["configuration_info"]
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
    if "kafka_version" in value:
        out["kafkaVersion"] = value["kafka_version"]
    if "logging_info" in value:
        import aws_sdk_kafka.types.logging_info

        out["loggingInfo"] = aws_sdk_kafka.types.logging_info.serialize_json(
            value["logging_info"]
        )
    if "number_of_broker_nodes" in value:
        out["numberOfBrokerNodes"] = value["number_of_broker_nodes"]
    if "storage_mode" in value:
        import aws_sdk_kafka.types.storage_mode

        out["storageMode"] = aws_sdk_kafka.types.storage_mode.serialize_json(
            value["storage_mode"]
        )
    return out


def deserialize_json(data: dict) -> ProvisionedRequest:
    out: ProvisionedRequest = {}  # type: ignore[typeddict-item]
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
    if "configurationInfo" in data:
        import aws_sdk_kafka.types.configuration_info

        out["configuration_info"] = (
            aws_sdk_kafka.types.configuration_info.deserialize_json(
                data["configurationInfo"]
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
    if "kafkaVersion" in data:
        out["kafka_version"] = data["kafkaVersion"]
    if "loggingInfo" in data:
        import aws_sdk_kafka.types.logging_info

        out["logging_info"] = aws_sdk_kafka.types.logging_info.deserialize_json(
            data["loggingInfo"]
        )
    if "numberOfBrokerNodes" in data:
        out["number_of_broker_nodes"] = data["numberOfBrokerNodes"]
    if "storageMode" in data:
        import aws_sdk_kafka.types.storage_mode

        out["storage_mode"] = aws_sdk_kafka.types.storage_mode.deserialize_json(
            data["storageMode"]
        )
    return out
