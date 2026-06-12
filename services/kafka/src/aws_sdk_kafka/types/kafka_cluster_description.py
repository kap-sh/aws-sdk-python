"""Generated from Smithy shape ``com.amazonaws.kafka#KafkaClusterDescription``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kafka.types.__string
    import aws_sdk_kafka.types.amazon_msk_cluster
    import aws_sdk_kafka.types.apache_kafka_cluster
    import aws_sdk_kafka.types.kafka_cluster_client_authentication
    import aws_sdk_kafka.types.kafka_cluster_client_vpc_config
    import aws_sdk_kafka.types.kafka_cluster_encryption_in_transit


class KafkaClusterDescription(TypedDict):
    amazon_msk_cluster: NotRequired[
        "aws_sdk_kafka.types.amazon_msk_cluster.AmazonMskCluster"
    ]
    """<p>Details of an Amazon MSK Cluster.</p>"""
    apache_kafka_cluster: NotRequired[
        "aws_sdk_kafka.types.apache_kafka_cluster.ApacheKafkaCluster"
    ]
    """<p>Details of an Apache Kafka Cluster.</p>"""
    kafka_cluster_alias: NotRequired["aws_sdk_kafka.types.__string.__string"]
    """<p>The alias of the Kafka cluster. Used to prefix names of replicated topics.</p>"""
    vpc_config: NotRequired[
        "aws_sdk_kafka.types.kafka_cluster_client_vpc_config.KafkaClusterClientVpcConfig"
    ]
    """<p>Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.</p>"""
    client_authentication: NotRequired[
        "aws_sdk_kafka.types.kafka_cluster_client_authentication.KafkaClusterClientAuthentication"
    ]
    """<p>Details of the client authentication used by the Apache Kafka cluster.</p>"""
    encryption_in_transit: NotRequired[
        "aws_sdk_kafka.types.kafka_cluster_encryption_in_transit.KafkaClusterEncryptionInTransit"
    ]
    """<p>Details of encryption in transit to the Apache Kafka cluster.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: KafkaClusterDescription) -> dict:
    out: dict = {}
    if "amazon_msk_cluster" in value:
        import aws_sdk_kafka.types.amazon_msk_cluster

        out["amazonMskCluster"] = aws_sdk_kafka.types.amazon_msk_cluster.serialize_json(
            value["amazon_msk_cluster"]
        )
    if "apache_kafka_cluster" in value:
        import aws_sdk_kafka.types.apache_kafka_cluster

        out["apacheKafkaCluster"] = (
            aws_sdk_kafka.types.apache_kafka_cluster.serialize_json(
                value["apache_kafka_cluster"]
            )
        )
    if "kafka_cluster_alias" in value:
        out["kafkaClusterAlias"] = value["kafka_cluster_alias"]
    if "vpc_config" in value:
        import aws_sdk_kafka.types.kafka_cluster_client_vpc_config

        out["vpcConfig"] = (
            aws_sdk_kafka.types.kafka_cluster_client_vpc_config.serialize_json(
                value["vpc_config"]
            )
        )
    if "client_authentication" in value:
        import aws_sdk_kafka.types.kafka_cluster_client_authentication

        out["clientAuthentication"] = (
            aws_sdk_kafka.types.kafka_cluster_client_authentication.serialize_json(
                value["client_authentication"]
            )
        )
    if "encryption_in_transit" in value:
        import aws_sdk_kafka.types.kafka_cluster_encryption_in_transit

        out["encryptionInTransit"] = (
            aws_sdk_kafka.types.kafka_cluster_encryption_in_transit.serialize_json(
                value["encryption_in_transit"]
            )
        )
    return out


def deserialize_json(data: dict) -> KafkaClusterDescription:
    out: KafkaClusterDescription = {}  # type: ignore[typeddict-item]
    if "amazonMskCluster" in data:
        import aws_sdk_kafka.types.amazon_msk_cluster

        out["amazon_msk_cluster"] = (
            aws_sdk_kafka.types.amazon_msk_cluster.deserialize_json(
                data["amazonMskCluster"]
            )
        )
    if "apacheKafkaCluster" in data:
        import aws_sdk_kafka.types.apache_kafka_cluster

        out["apache_kafka_cluster"] = (
            aws_sdk_kafka.types.apache_kafka_cluster.deserialize_json(
                data["apacheKafkaCluster"]
            )
        )
    if "kafkaClusterAlias" in data:
        out["kafka_cluster_alias"] = data["kafkaClusterAlias"]
    if "vpcConfig" in data:
        import aws_sdk_kafka.types.kafka_cluster_client_vpc_config

        out["vpc_config"] = (
            aws_sdk_kafka.types.kafka_cluster_client_vpc_config.deserialize_json(
                data["vpcConfig"]
            )
        )
    if "clientAuthentication" in data:
        import aws_sdk_kafka.types.kafka_cluster_client_authentication

        out["client_authentication"] = (
            aws_sdk_kafka.types.kafka_cluster_client_authentication.deserialize_json(
                data["clientAuthentication"]
            )
        )
    if "encryptionInTransit" in data:
        import aws_sdk_kafka.types.kafka_cluster_encryption_in_transit

        out["encryption_in_transit"] = (
            aws_sdk_kafka.types.kafka_cluster_encryption_in_transit.deserialize_json(
                data["encryptionInTransit"]
            )
        )
    return out
