"""Generated from Smithy shape ``com.amazonaws.pipes#PipeSourceSelfManagedKafkaParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.kafka_bootstrap_servers
    import aws_sdk_pipes.types.kafka_topic_name
    import aws_sdk_pipes.types.limit_max10000
    import aws_sdk_pipes.types.maximum_batching_window_in_seconds
    import aws_sdk_pipes.types.secret_manager_arn
    import aws_sdk_pipes.types.self_managed_kafka_access_configuration_credentials
    import aws_sdk_pipes.types.self_managed_kafka_access_configuration_vpc
    import aws_sdk_pipes.types.self_managed_kafka_start_position
    import aws_sdk_pipes.types.uri


class PipeSourceSelfManagedKafkaParameters(TypedDict):
    topic_name: "aws_sdk_pipes.types.kafka_topic_name.KafkaTopicName"
    """<p>The name of the topic that the pipe will read from.</p>"""
    starting_position: NotRequired[
        "aws_sdk_pipes.types.self_managed_kafka_start_position.SelfManagedKafkaStartPosition"
    ]
    """<p>The position in a stream from which to start reading.</p>"""
    additional_bootstrap_servers: NotRequired[
        "aws_sdk_pipes.types.kafka_bootstrap_servers.KafkaBootstrapServers"
    ]
    """<p>An array of server URLs.</p>"""
    batch_size: NotRequired["aws_sdk_pipes.types.limit_max10000.LimitMax10000"]
    """<p>The maximum number of records to include in each batch.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "aws_sdk_pipes.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum length of a time to wait for events.</p>"""
    consumer_group_id: NotRequired["aws_sdk_pipes.types.uri.URI"]
    """<p>The name of the destination queue to consume.</p>"""
    credentials: NotRequired[
        "aws_sdk_pipes.types.self_managed_kafka_access_configuration_credentials.SelfManagedKafkaAccessConfigurationCredentials"
    ]
    """<p>The credentials needed to access the resource.</p>"""
    server_root_ca_certificate: NotRequired[
        "aws_sdk_pipes.types.secret_manager_arn.SecretManagerArn"
    ]
    """<p>The ARN of the Secrets Manager secret used for certification.</p>"""
    vpc: NotRequired[
        "aws_sdk_pipes.types.self_managed_kafka_access_configuration_vpc.SelfManagedKafkaAccessConfigurationVpc"
    ]
    """<p>This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeSourceSelfManagedKafkaParameters) -> dict:
    out: dict = {}
    out["TopicName"] = value["topic_name"]
    if "starting_position" in value:
        out["StartingPosition"] = value["starting_position"]
    if "additional_bootstrap_servers" in value:
        import aws_sdk_pipes.types.kafka_bootstrap_servers

        out["AdditionalBootstrapServers"] = (
            aws_sdk_pipes.types.kafka_bootstrap_servers.serialize_json(
                value["additional_bootstrap_servers"]
            )
        )
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "consumer_group_id" in value:
        out["ConsumerGroupID"] = value["consumer_group_id"]
    if "credentials" in value:
        import aws_sdk_pipes.types.self_managed_kafka_access_configuration_credentials

        out["Credentials"] = (
            aws_sdk_pipes.types.self_managed_kafka_access_configuration_credentials.serialize_json(
                value["credentials"]
            )
        )
    if "server_root_ca_certificate" in value:
        out["ServerRootCaCertificate"] = value["server_root_ca_certificate"]
    if "vpc" in value:
        import aws_sdk_pipes.types.self_managed_kafka_access_configuration_vpc

        out["Vpc"] = (
            aws_sdk_pipes.types.self_managed_kafka_access_configuration_vpc.serialize_json(
                value["vpc"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeSourceSelfManagedKafkaParameters:
    out: PipeSourceSelfManagedKafkaParameters = {}  # type: ignore[typeddict-item]
    if "TopicName" in data:
        out["topic_name"] = data["TopicName"]
    else:
        raise DeserializationError(
            "PipeSourceSelfManagedKafkaParameters.topic_name required"
        )
    if "StartingPosition" in data:
        out["starting_position"] = data["StartingPosition"]
    if "AdditionalBootstrapServers" in data:
        import aws_sdk_pipes.types.kafka_bootstrap_servers

        out["additional_bootstrap_servers"] = (
            aws_sdk_pipes.types.kafka_bootstrap_servers.deserialize_json(
                data["AdditionalBootstrapServers"]
            )
        )
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if "ConsumerGroupID" in data:
        out["consumer_group_id"] = data["ConsumerGroupID"]
    if "Credentials" in data:
        import aws_sdk_pipes.types.self_managed_kafka_access_configuration_credentials

        out["credentials"] = (
            aws_sdk_pipes.types.self_managed_kafka_access_configuration_credentials.deserialize_json(
                data["Credentials"]
            )
        )
    if "ServerRootCaCertificate" in data:
        out["server_root_ca_certificate"] = data["ServerRootCaCertificate"]
    if "Vpc" in data:
        import aws_sdk_pipes.types.self_managed_kafka_access_configuration_vpc

        out["vpc"] = (
            aws_sdk_pipes.types.self_managed_kafka_access_configuration_vpc.deserialize_json(
                data["Vpc"]
            )
        )
    return out
