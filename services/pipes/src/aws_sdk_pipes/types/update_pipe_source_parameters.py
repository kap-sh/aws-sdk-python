"""Generated from Smithy shape ``com.amazonaws.pipes#UpdatePipeSourceParameters``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_pipes.types.filter_criteria
    import aws_sdk_pipes.types.update_pipe_source_active_mq_broker_parameters
    import aws_sdk_pipes.types.update_pipe_source_dynamo_db_stream_parameters
    import aws_sdk_pipes.types.update_pipe_source_kinesis_stream_parameters
    import aws_sdk_pipes.types.update_pipe_source_managed_streaming_kafka_parameters
    import aws_sdk_pipes.types.update_pipe_source_rabbit_mq_broker_parameters
    import aws_sdk_pipes.types.update_pipe_source_self_managed_kafka_parameters
    import aws_sdk_pipes.types.update_pipe_source_sqs_queue_parameters


class UpdatePipeSourceParameters(TypedDict):
    filter_criteria: NotRequired["aws_sdk_pipes.types.filter_criteria.FilterCriteria"]
    """<p>The collection of event patterns used to filter events.</p> <p>To remove a filter, specify a <code>FilterCriteria</code> object with an empty array of <code>Filter</code> objects.</p> <p>For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eventbridge-and-event-patterns.html\">Events and Event Patterns</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""
    kinesis_stream_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_kinesis_stream_parameters.UpdatePipeSourceKinesisStreamParameters"
    ]
    """<p>The parameters for using a Kinesis stream as a source.</p>"""
    dynamo_db_stream_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_dynamo_db_stream_parameters.UpdatePipeSourceDynamoDBStreamParameters"
    ]
    """<p>The parameters for using a DynamoDB stream as a source.</p>"""
    sqs_queue_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_sqs_queue_parameters.UpdatePipeSourceSqsQueueParameters"
    ]
    """<p>The parameters for using a Amazon SQS stream as a source.</p>"""
    active_mq_broker_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_active_mq_broker_parameters.UpdatePipeSourceActiveMQBrokerParameters"
    ]
    """<p>The parameters for using an Active MQ broker as a source.</p>"""
    rabbit_mq_broker_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_rabbit_mq_broker_parameters.UpdatePipeSourceRabbitMQBrokerParameters"
    ]
    """<p>The parameters for using a Rabbit MQ broker as a source.</p>"""
    managed_streaming_kafka_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_managed_streaming_kafka_parameters.UpdatePipeSourceManagedStreamingKafkaParameters"
    ]
    """<p>The parameters for using an MSK stream as a source.</p>"""
    self_managed_kafka_parameters: NotRequired[
        "aws_sdk_pipes.types.update_pipe_source_self_managed_kafka_parameters.UpdatePipeSourceSelfManagedKafkaParameters"
    ]
    """<p>The parameters for using a self-managed Apache Kafka stream as a source.</p> <p>A <i>self managed</i> cluster refers to any Apache Kafka cluster not hosted by Amazon Web Services. This includes both clusters you manage yourself, as well as those hosted by a third-party provider, such as <a href=\"https://www.confluent.io/\">Confluent Cloud</a>, <a href=\"https://www.cloudkarafka.com/\">CloudKarafka</a>, or <a href=\"https://redpanda.com/\">Redpanda</a>. For more information, see <a href=\"https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-pipes-kafka.html\">Apache Kafka streams as a source</a> in the <i>Amazon EventBridge User Guide</i>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdatePipeSourceParameters) -> dict:
    out: dict = {}
    if "filter_criteria" in value:
        import aws_sdk_pipes.types.filter_criteria

        out["FilterCriteria"] = aws_sdk_pipes.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "kinesis_stream_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_kinesis_stream_parameters

        out["KinesisStreamParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_kinesis_stream_parameters.serialize_json(
                value["kinesis_stream_parameters"]
            )
        )
    if "dynamo_db_stream_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_dynamo_db_stream_parameters

        out["DynamoDBStreamParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_dynamo_db_stream_parameters.serialize_json(
                value["dynamo_db_stream_parameters"]
            )
        )
    if "sqs_queue_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_sqs_queue_parameters

        out["SqsQueueParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_sqs_queue_parameters.serialize_json(
                value["sqs_queue_parameters"]
            )
        )
    if "active_mq_broker_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_active_mq_broker_parameters

        out["ActiveMQBrokerParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_active_mq_broker_parameters.serialize_json(
                value["active_mq_broker_parameters"]
            )
        )
    if "rabbit_mq_broker_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_rabbit_mq_broker_parameters

        out["RabbitMQBrokerParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_rabbit_mq_broker_parameters.serialize_json(
                value["rabbit_mq_broker_parameters"]
            )
        )
    if "managed_streaming_kafka_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_managed_streaming_kafka_parameters

        out["ManagedStreamingKafkaParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_managed_streaming_kafka_parameters.serialize_json(
                value["managed_streaming_kafka_parameters"]
            )
        )
    if "self_managed_kafka_parameters" in value:
        import aws_sdk_pipes.types.update_pipe_source_self_managed_kafka_parameters

        out["SelfManagedKafkaParameters"] = (
            aws_sdk_pipes.types.update_pipe_source_self_managed_kafka_parameters.serialize_json(
                value["self_managed_kafka_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdatePipeSourceParameters:
    out: UpdatePipeSourceParameters = {}  # type: ignore[typeddict-item]
    if "FilterCriteria" in data:
        import aws_sdk_pipes.types.filter_criteria

        out["filter_criteria"] = aws_sdk_pipes.types.filter_criteria.deserialize_json(
            data["FilterCriteria"]
        )
    if "KinesisStreamParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_kinesis_stream_parameters

        out["kinesis_stream_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_kinesis_stream_parameters.deserialize_json(
                data["KinesisStreamParameters"]
            )
        )
    if "DynamoDBStreamParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_dynamo_db_stream_parameters

        out["dynamo_db_stream_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_dynamo_db_stream_parameters.deserialize_json(
                data["DynamoDBStreamParameters"]
            )
        )
    if "SqsQueueParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_sqs_queue_parameters

        out["sqs_queue_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_sqs_queue_parameters.deserialize_json(
                data["SqsQueueParameters"]
            )
        )
    if "ActiveMQBrokerParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_active_mq_broker_parameters

        out["active_mq_broker_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_active_mq_broker_parameters.deserialize_json(
                data["ActiveMQBrokerParameters"]
            )
        )
    if "RabbitMQBrokerParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_rabbit_mq_broker_parameters

        out["rabbit_mq_broker_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_rabbit_mq_broker_parameters.deserialize_json(
                data["RabbitMQBrokerParameters"]
            )
        )
    if "ManagedStreamingKafkaParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_managed_streaming_kafka_parameters

        out["managed_streaming_kafka_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_managed_streaming_kafka_parameters.deserialize_json(
                data["ManagedStreamingKafkaParameters"]
            )
        )
    if "SelfManagedKafkaParameters" in data:
        import aws_sdk_pipes.types.update_pipe_source_self_managed_kafka_parameters

        out["self_managed_kafka_parameters"] = (
            aws_sdk_pipes.types.update_pipe_source_self_managed_kafka_parameters.deserialize_json(
                data["SelfManagedKafkaParameters"]
            )
        )
    return out
