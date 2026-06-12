"""Generated from Smithy shape ``com.amazonaws.kafkaconnect#DescribeConnectorResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafkaconnect.types.__list_of_plugin_description
    import aws_sdk_kafkaconnect.types.__string
    import aws_sdk_kafkaconnect.types.__timestamp_iso8601
    import aws_sdk_kafkaconnect.types.capacity_description
    import aws_sdk_kafkaconnect.types.connector_configuration
    import aws_sdk_kafkaconnect.types.connector_state
    import aws_sdk_kafkaconnect.types.kafka_cluster_client_authentication_description
    import aws_sdk_kafkaconnect.types.kafka_cluster_description
    import aws_sdk_kafkaconnect.types.kafka_cluster_encryption_in_transit_description
    import aws_sdk_kafkaconnect.types.log_delivery_description
    import aws_sdk_kafkaconnect.types.network_type
    import aws_sdk_kafkaconnect.types.state_description
    import aws_sdk_kafkaconnect.types.worker_configuration_description


class DescribeConnectorResponse(TypedDict):
    capacity: NotRequired[
        "aws_sdk_kafkaconnect.types.capacity_description.CapacityDescription"
    ]
    """<p>Information about the capacity of the connector, whether it is auto scaled or provisioned.</p>"""
    connector_arn: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The Amazon Resource Name (ARN) of the connector.</p>"""
    connector_configuration: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_configuration.ConnectorConfiguration"
    ]
    """<p>A map of keys to values that represent the configuration for the connector.</p>"""
    connector_description: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>A summary description of the connector.</p>"""
    connector_name: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The name of the connector.</p>"""
    connector_state: NotRequired[
        "aws_sdk_kafkaconnect.types.connector_state.ConnectorState"
    ]
    """<p>The state of the connector.</p>"""
    creation_time: NotRequired[
        "aws_sdk_kafkaconnect.types.__timestamp_iso8601.__timestampIso8601"
    ]
    """<p>The time the connector was created.</p>"""
    current_version: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The current version of the connector.</p>"""
    kafka_cluster: NotRequired[
        "aws_sdk_kafkaconnect.types.kafka_cluster_description.KafkaClusterDescription"
    ]
    """<p>The Apache Kafka cluster that the connector is connected to.</p>"""
    kafka_cluster_client_authentication: NotRequired[
        "aws_sdk_kafkaconnect.types.kafka_cluster_client_authentication_description.KafkaClusterClientAuthenticationDescription"
    ]
    """<p>The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.</p>"""
    kafka_cluster_encryption_in_transit: NotRequired[
        "aws_sdk_kafkaconnect.types.kafka_cluster_encryption_in_transit_description.KafkaClusterEncryptionInTransitDescription"
    ]
    """<p>Details of encryption in transit to the Apache Kafka cluster.</p>"""
    kafka_connect_version: NotRequired["aws_sdk_kafkaconnect.types.__string.__string"]
    """<p>The version of Kafka Connect. It has to be compatible with both the Apache Kafka cluster's version and the plugins.</p>"""
    log_delivery: NotRequired[
        "aws_sdk_kafkaconnect.types.log_delivery_description.LogDeliveryDescription"
    ]
    """<p>Details about delivering logs to Amazon CloudWatch Logs.</p>"""
    network_type: NotRequired["aws_sdk_kafkaconnect.types.network_type.NetworkType"]
    """<p>The network type of the connector. It gives connectors connectivity to either IPv4 (IPV4) or IPv4 and IPv6 (DUAL) destinations. Defaults to IPV4.</p>"""
    plugins: NotRequired[
        "aws_sdk_kafkaconnect.types.__list_of_plugin_description.__listOfPluginDescription"
    ]
    """<p>Specifies which plugins were used for this connector.</p>"""
    service_execution_role_arn: NotRequired[
        "aws_sdk_kafkaconnect.types.__string.__string"
    ]
    """<p>The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.</p>"""
    worker_configuration: NotRequired[
        "aws_sdk_kafkaconnect.types.worker_configuration_description.WorkerConfigurationDescription"
    ]
    """<p>Specifies which worker configuration was used for the connector.</p>"""
    state_description: NotRequired[
        "aws_sdk_kafkaconnect.types.state_description.StateDescription"
    ]
    """<p>Details about the state of a connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeConnectorResponse) -> dict:
    out: dict = {}
    if "capacity" in value:
        import aws_sdk_kafkaconnect.types.capacity_description

        out["capacity"] = (
            aws_sdk_kafkaconnect.types.capacity_description.serialize_json(
                value["capacity"]
            )
        )
    if "connector_arn" in value:
        out["connectorArn"] = value["connector_arn"]
    if "connector_configuration" in value:
        import aws_sdk_kafkaconnect.types.connector_configuration

        out["connectorConfiguration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration.serialize_json(
                value["connector_configuration"]
            )
        )
    if "connector_description" in value:
        out["connectorDescription"] = value["connector_description"]
    if "connector_name" in value:
        out["connectorName"] = value["connector_name"]
    if "connector_state" in value:
        out["connectorState"] = value["connector_state"]
    if "creation_time" in value:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creationTime"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.serialize_json(
                value["creation_time"]
            )
        )
    if "current_version" in value:
        out["currentVersion"] = value["current_version"]
    if "kafka_cluster" in value:
        import aws_sdk_kafkaconnect.types.kafka_cluster_description

        out["kafkaCluster"] = (
            aws_sdk_kafkaconnect.types.kafka_cluster_description.serialize_json(
                value["kafka_cluster"]
            )
        )
    if "kafka_cluster_client_authentication" in value:
        import aws_sdk_kafkaconnect.types.kafka_cluster_client_authentication_description

        out["kafkaClusterClientAuthentication"] = (
            aws_sdk_kafkaconnect.types.kafka_cluster_client_authentication_description.serialize_json(
                value["kafka_cluster_client_authentication"]
            )
        )
    if "kafka_cluster_encryption_in_transit" in value:
        import aws_sdk_kafkaconnect.types.kafka_cluster_encryption_in_transit_description

        out["kafkaClusterEncryptionInTransit"] = (
            aws_sdk_kafkaconnect.types.kafka_cluster_encryption_in_transit_description.serialize_json(
                value["kafka_cluster_encryption_in_transit"]
            )
        )
    if "kafka_connect_version" in value:
        out["kafkaConnectVersion"] = value["kafka_connect_version"]
    if "log_delivery" in value:
        import aws_sdk_kafkaconnect.types.log_delivery_description

        out["logDelivery"] = (
            aws_sdk_kafkaconnect.types.log_delivery_description.serialize_json(
                value["log_delivery"]
            )
        )
    if "network_type" in value:
        out["networkType"] = value["network_type"]
    if "plugins" in value:
        import aws_sdk_kafkaconnect.types.__list_of_plugin_description

        out["plugins"] = (
            aws_sdk_kafkaconnect.types.__list_of_plugin_description.serialize_json(
                value["plugins"]
            )
        )
    if "service_execution_role_arn" in value:
        out["serviceExecutionRoleArn"] = value["service_execution_role_arn"]
    if "worker_configuration" in value:
        import aws_sdk_kafkaconnect.types.worker_configuration_description

        out["workerConfiguration"] = (
            aws_sdk_kafkaconnect.types.worker_configuration_description.serialize_json(
                value["worker_configuration"]
            )
        )
    if "state_description" in value:
        import aws_sdk_kafkaconnect.types.state_description

        out["stateDescription"] = (
            aws_sdk_kafkaconnect.types.state_description.serialize_json(
                value["state_description"]
            )
        )
    return out


def deserialize_json(data: dict) -> DescribeConnectorResponse:
    out: DescribeConnectorResponse = {}  # type: ignore[typeddict-item]
    if "capacity" in data:
        import aws_sdk_kafkaconnect.types.capacity_description

        out["capacity"] = (
            aws_sdk_kafkaconnect.types.capacity_description.deserialize_json(
                data["capacity"]
            )
        )
    if "connectorArn" in data:
        out["connector_arn"] = data["connectorArn"]
    if "connectorConfiguration" in data:
        import aws_sdk_kafkaconnect.types.connector_configuration

        out["connector_configuration"] = (
            aws_sdk_kafkaconnect.types.connector_configuration.deserialize_json(
                data["connectorConfiguration"]
            )
        )
    if "connectorDescription" in data:
        out["connector_description"] = data["connectorDescription"]
    if "connectorName" in data:
        out["connector_name"] = data["connectorName"]
    if "connectorState" in data:
        out["connector_state"] = data["connectorState"]
    if "creationTime" in data:
        import aws_sdk_kafkaconnect.types.__timestamp_iso8601

        out["creation_time"] = (
            aws_sdk_kafkaconnect.types.__timestamp_iso8601.deserialize_json(
                data["creationTime"]
            )
        )
    if "currentVersion" in data:
        out["current_version"] = data["currentVersion"]
    if "kafkaCluster" in data:
        import aws_sdk_kafkaconnect.types.kafka_cluster_description

        out["kafka_cluster"] = (
            aws_sdk_kafkaconnect.types.kafka_cluster_description.deserialize_json(
                data["kafkaCluster"]
            )
        )
    if "kafkaClusterClientAuthentication" in data:
        import aws_sdk_kafkaconnect.types.kafka_cluster_client_authentication_description

        out["kafka_cluster_client_authentication"] = (
            aws_sdk_kafkaconnect.types.kafka_cluster_client_authentication_description.deserialize_json(
                data["kafkaClusterClientAuthentication"]
            )
        )
    if "kafkaClusterEncryptionInTransit" in data:
        import aws_sdk_kafkaconnect.types.kafka_cluster_encryption_in_transit_description

        out["kafka_cluster_encryption_in_transit"] = (
            aws_sdk_kafkaconnect.types.kafka_cluster_encryption_in_transit_description.deserialize_json(
                data["kafkaClusterEncryptionInTransit"]
            )
        )
    if "kafkaConnectVersion" in data:
        out["kafka_connect_version"] = data["kafkaConnectVersion"]
    if "logDelivery" in data:
        import aws_sdk_kafkaconnect.types.log_delivery_description

        out["log_delivery"] = (
            aws_sdk_kafkaconnect.types.log_delivery_description.deserialize_json(
                data["logDelivery"]
            )
        )
    if "networkType" in data:
        out["network_type"] = data["networkType"]
    if "plugins" in data:
        import aws_sdk_kafkaconnect.types.__list_of_plugin_description

        out["plugins"] = (
            aws_sdk_kafkaconnect.types.__list_of_plugin_description.deserialize_json(
                data["plugins"]
            )
        )
    if "serviceExecutionRoleArn" in data:
        out["service_execution_role_arn"] = data["serviceExecutionRoleArn"]
    if "workerConfiguration" in data:
        import aws_sdk_kafkaconnect.types.worker_configuration_description

        out["worker_configuration"] = (
            aws_sdk_kafkaconnect.types.worker_configuration_description.deserialize_json(
                data["workerConfiguration"]
            )
        )
    if "stateDescription" in data:
        import aws_sdk_kafkaconnect.types.state_description

        out["state_description"] = (
            aws_sdk_kafkaconnect.types.state_description.deserialize_json(
                data["stateDescription"]
            )
        )
    return out
