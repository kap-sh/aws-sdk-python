"""Generated from Smithy shape ``com.amazonaws.lambda#CreateEventSourceMappingRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from aws_sdk_lambda.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_lambda.types.amazon_managed_kafka_event_source_config
    import aws_sdk_lambda.types.arn
    import aws_sdk_lambda.types.batch_size
    import aws_sdk_lambda.types.bisect_batch_on_function_error
    import aws_sdk_lambda.types.date
    import aws_sdk_lambda.types.destination_config
    import aws_sdk_lambda.types.document_db_event_source_config
    import aws_sdk_lambda.types.enabled
    import aws_sdk_lambda.types.event_source_mapping_logging_config
    import aws_sdk_lambda.types.event_source_mapping_metrics_config
    import aws_sdk_lambda.types.event_source_position
    import aws_sdk_lambda.types.filter_criteria
    import aws_sdk_lambda.types.function_response_type_list
    import aws_sdk_lambda.types.kms_key_arn
    import aws_sdk_lambda.types.maximum_batching_window_in_seconds
    import aws_sdk_lambda.types.maximum_record_age_in_seconds
    import aws_sdk_lambda.types.maximum_retry_attempts_event_source_mapping
    import aws_sdk_lambda.types.namespaced_function_name
    import aws_sdk_lambda.types.parallelization_factor
    import aws_sdk_lambda.types.provisioned_poller_config
    import aws_sdk_lambda.types.queues
    import aws_sdk_lambda.types.scaling_config
    import aws_sdk_lambda.types.self_managed_event_source
    import aws_sdk_lambda.types.self_managed_kafka_event_source_config
    import aws_sdk_lambda.types.source_access_configurations
    import aws_sdk_lambda.types.tags
    import aws_sdk_lambda.types.topics
    import aws_sdk_lambda.types.tumbling_window_in_seconds


class CreateEventSourceMappingRequest(TypedDict, closed=True):
    event_source_arn: NotRequired["aws_sdk_lambda.types.arn.Arn"]
    r"""<p>The Amazon Resource Name (ARN) of the event source.</p> <ul> <li> <p> <b>Amazon Kinesis</b> – The ARN of the data stream or a stream consumer.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – The ARN of the stream.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – The ARN of the queue.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – The ARN of the cluster or the ARN of the VPC connection (for <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#msk-multi-vpc\">cross-account event source mappings</a>).</p> </li> <li> <p> <b>Amazon MQ</b> – The ARN of the broker.</p> </li> <li> <p> <b>Amazon DocumentDB</b> – The ARN of the DocumentDB change stream.</p> </li> </ul>"""
    function_name: (
        "aws_sdk_lambda.types.namespaced_function_name.NamespacedFunctionName"
    )
    r"""<p>The name or ARN of the Lambda function.</p> <p class=\"title\"> <b>Name formats</b> </p> <ul> <li> <p> <b>Function name</b> – <code>MyFunction</code>.</p> </li> <li> <p> <b>Function ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction</code>.</p> </li> <li> <p> <b>Version or Alias ARN</b> – <code>arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD</code>.</p> </li> <li> <p> <b>Partial ARN</b> – <code>123456789012:function:MyFunction</code>.</p> </li> </ul> <p>The length constraint applies only to the full ARN. If you specify only the function name, it's limited to 64 characters in length.</p>"""
    enabled: NotRequired["aws_sdk_lambda.types.enabled.Enabled"]
    """<p>When true, the event source mapping is active. When false, Lambda pauses polling and invocation.</p> <p>Default: True</p>"""
    batch_size: NotRequired["aws_sdk_lambda.types.batch_size.BatchSize"]
    """<p>The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).</p> <ul> <li> <p> <b>Amazon Kinesis</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon DynamoDB Streams</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon Simple Queue Service</b> – Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.</p> </li> <li> <p> <b>Amazon Managed Streaming for Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Self-managed Apache Kafka</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>Amazon MQ (ActiveMQ and RabbitMQ)</b> – Default 100. Max 10,000.</p> </li> <li> <p> <b>DocumentDB</b> – Default 100. Max 10,000.</p> </li> </ul>"""
    filter_criteria: NotRequired["aws_sdk_lambda.types.filter_criteria.FilterCriteria"]
    r"""<p>An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html\">Lambda event filtering</a>.</p>"""
    maximum_batching_window_in_seconds: NotRequired[
        "aws_sdk_lambda.types.maximum_batching_window_in_seconds.MaximumBatchingWindowInSeconds"
    ]
    """<p>The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure <code>MaximumBatchingWindowInSeconds</code> to any value from 0 seconds to 300 seconds in increments of seconds.</p> <p>For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change <code>MaximumBatchingWindowInSeconds</code> in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.</p> <p>Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set <code>BatchSize</code> to a value greater than 10, you must set <code>MaximumBatchingWindowInSeconds</code> to at least 1.</p>"""
    parallelization_factor: NotRequired[
        "aws_sdk_lambda.types.parallelization_factor.ParallelizationFactor"
    ]
    """<p>(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.</p>"""
    starting_position: NotRequired[
        "aws_sdk_lambda.types.event_source_position.EventSourcePosition"
    ]
    """<p>The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. <code>AT_TIMESTAMP</code> is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.</p>"""
    starting_position_timestamp: NotRequired["aws_sdk_lambda.types.date.Date"]
    """<p>With <code>StartingPosition</code> set to <code>AT_TIMESTAMP</code>, the time from which to start reading. <code>StartingPositionTimestamp</code> cannot be in the future.</p>"""
    destination_config: NotRequired[
        "aws_sdk_lambda.types.destination_config.DestinationConfig"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) A configuration object that specifies the destination of an event after Lambda processes it.</p>"""
    maximum_record_age_in_seconds: NotRequired[
        "aws_sdk_lambda.types.maximum_record_age_in_seconds.MaximumRecordAgeInSeconds"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records older than the specified age. The default value is infinite (-1).</p>"""
    bisect_batch_on_function_error: NotRequired[
        "aws_sdk_lambda.types.bisect_batch_on_function_error.BisectBatchOnFunctionError"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) If the function returns an error, split the batch in two and retry.</p>"""
    maximum_retry_attempts: NotRequired[
        "aws_sdk_lambda.types.maximum_retry_attempts_event_source_mapping.MaximumRetryAttemptsEventSourceMapping"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.</p>"""
    tags: NotRequired["aws_sdk_lambda.types.tags.Tags"]
    """<p>A list of tags to apply to the event source mapping.</p>"""
    tumbling_window_in_seconds: NotRequired[
        "aws_sdk_lambda.types.tumbling_window_in_seconds.TumblingWindowInSeconds"
    ]
    """<p>(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.</p>"""
    topics: NotRequired["aws_sdk_lambda.types.topics.Topics"]
    """<p>The name of the Kafka topic.</p>"""
    queues: NotRequired["aws_sdk_lambda.types.queues.Queues"]
    """<p> (MQ) The name of the Amazon MQ broker destination queue to consume. </p>"""
    source_access_configurations: NotRequired[
        "aws_sdk_lambda.types.source_access_configurations.SourceAccessConfigurations"
    ]
    """<p>An array of authentication protocols or VPC components required to secure your event source.</p>"""
    self_managed_event_source: NotRequired[
        "aws_sdk_lambda.types.self_managed_event_source.SelfManagedEventSource"
    ]
    """<p>The self-managed Apache Kafka cluster to receive records from.</p>"""
    function_response_types: NotRequired[
        "aws_sdk_lambda.types.function_response_type_list.FunctionResponseTypeList"
    ]
    """<p>(Kinesis, DynamoDB Streams, Amazon MSK, self-managed Apache Kafka, and Amazon SQS) A list of current response type enums applied to the event source mapping.</p>"""
    amazon_managed_kafka_event_source_config: NotRequired[
        "aws_sdk_lambda.types.amazon_managed_kafka_event_source_config.AmazonManagedKafkaEventSourceConfig"
    ]
    """<p>Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.</p>"""
    self_managed_kafka_event_source_config: NotRequired[
        "aws_sdk_lambda.types.self_managed_kafka_event_source_config.SelfManagedKafkaEventSourceConfig"
    ]
    """<p>Specific configuration settings for a self-managed Apache Kafka event source.</p>"""
    scaling_config: NotRequired["aws_sdk_lambda.types.scaling_config.ScalingConfig"]
    r"""<p>(Amazon SQS only) The scaling configuration for the event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency\">Configuring maximum concurrency for Amazon SQS event sources</a>.</p>"""
    document_db_event_source_config: NotRequired[
        "aws_sdk_lambda.types.document_db_event_source_config.DocumentDBEventSourceConfig"
    ]
    """<p>Specific configuration settings for a DocumentDB event source.</p>"""
    kms_key_arn: NotRequired["aws_sdk_lambda.types.kms_key_arn.KMSKeyArn"]
    r"""<p> The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your function's <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics\">filter criteria</a>. By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key. </p>"""
    metrics_config: NotRequired[
        "aws_sdk_lambda.types.event_source_mapping_metrics_config.EventSourceMappingMetricsConfig"
    ]
    r"""<p>The metrics configuration for your event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics\">Event source mapping metrics</a>.</p>"""
    logging_config: NotRequired[
        "aws_sdk_lambda.types.event_source_mapping_logging_config.EventSourceMappingLoggingConfig"
    ]
    r"""<p>(Amazon MSK, and self-managed Apache Kafka only) The logging configuration for your event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/esm-logging.html\">Event source mapping logging</a>.</p>"""
    provisioned_poller_config: NotRequired[
        "aws_sdk_lambda.types.provisioned_poller_config.ProvisionedPollerConfig"
    ]
    r"""<p>(Amazon SQS, Amazon MSK, and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see <a href=\"https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode\">provisioned mode</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateEventSourceMappingRequest) -> dict:
    out: dict = {}
    if "event_source_arn" in value:
        out["EventSourceArn"] = value["event_source_arn"]
    out["FunctionName"] = value["function_name"]
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "batch_size" in value:
        out["BatchSize"] = value["batch_size"]
    if "filter_criteria" in value:
        import aws_sdk_lambda.types.filter_criteria

        out["FilterCriteria"] = aws_sdk_lambda.types.filter_criteria.serialize_json(
            value["filter_criteria"]
        )
    if "maximum_batching_window_in_seconds" in value:
        out["MaximumBatchingWindowInSeconds"] = value[
            "maximum_batching_window_in_seconds"
        ]
    if "parallelization_factor" in value:
        out["ParallelizationFactor"] = value["parallelization_factor"]
    if "starting_position" in value:
        import aws_sdk_lambda.types.event_source_position

        out["StartingPosition"] = (
            aws_sdk_lambda.types.event_source_position.serialize_json(
                value["starting_position"]
            )
        )
    if "starting_position_timestamp" in value:
        import aws_sdk_lambda.types.date

        out["StartingPositionTimestamp"] = aws_sdk_lambda.types.date.serialize_json(
            value["starting_position_timestamp"]
        )
    if "destination_config" in value:
        import aws_sdk_lambda.types.destination_config

        out["DestinationConfig"] = (
            aws_sdk_lambda.types.destination_config.serialize_json(
                value["destination_config"]
            )
        )
    if "maximum_record_age_in_seconds" in value:
        out["MaximumRecordAgeInSeconds"] = value["maximum_record_age_in_seconds"]
    if "bisect_batch_on_function_error" in value:
        out["BisectBatchOnFunctionError"] = value["bisect_batch_on_function_error"]
    if "maximum_retry_attempts" in value:
        out["MaximumRetryAttempts"] = value["maximum_retry_attempts"]
    if "tags" in value:
        import aws_sdk_lambda.types.tags

        out["Tags"] = aws_sdk_lambda.types.tags.serialize_json(value["tags"])
    if "tumbling_window_in_seconds" in value:
        out["TumblingWindowInSeconds"] = value["tumbling_window_in_seconds"]
    if "topics" in value:
        import aws_sdk_lambda.types.topics

        out["Topics"] = aws_sdk_lambda.types.topics.serialize_json(value["topics"])
    if "queues" in value:
        import aws_sdk_lambda.types.queues

        out["Queues"] = aws_sdk_lambda.types.queues.serialize_json(value["queues"])
    if "source_access_configurations" in value:
        import aws_sdk_lambda.types.source_access_configurations

        out["SourceAccessConfigurations"] = (
            aws_sdk_lambda.types.source_access_configurations.serialize_json(
                value["source_access_configurations"]
            )
        )
    if "self_managed_event_source" in value:
        import aws_sdk_lambda.types.self_managed_event_source

        out["SelfManagedEventSource"] = (
            aws_sdk_lambda.types.self_managed_event_source.serialize_json(
                value["self_managed_event_source"]
            )
        )
    if "function_response_types" in value:
        import aws_sdk_lambda.types.function_response_type_list

        out["FunctionResponseTypes"] = (
            aws_sdk_lambda.types.function_response_type_list.serialize_json(
                value["function_response_types"]
            )
        )
    if "amazon_managed_kafka_event_source_config" in value:
        import aws_sdk_lambda.types.amazon_managed_kafka_event_source_config

        out["AmazonManagedKafkaEventSourceConfig"] = (
            aws_sdk_lambda.types.amazon_managed_kafka_event_source_config.serialize_json(
                value["amazon_managed_kafka_event_source_config"]
            )
        )
    if "self_managed_kafka_event_source_config" in value:
        import aws_sdk_lambda.types.self_managed_kafka_event_source_config

        out["SelfManagedKafkaEventSourceConfig"] = (
            aws_sdk_lambda.types.self_managed_kafka_event_source_config.serialize_json(
                value["self_managed_kafka_event_source_config"]
            )
        )
    if "scaling_config" in value:
        import aws_sdk_lambda.types.scaling_config

        out["ScalingConfig"] = aws_sdk_lambda.types.scaling_config.serialize_json(
            value["scaling_config"]
        )
    if "document_db_event_source_config" in value:
        import aws_sdk_lambda.types.document_db_event_source_config

        out["DocumentDBEventSourceConfig"] = (
            aws_sdk_lambda.types.document_db_event_source_config.serialize_json(
                value["document_db_event_source_config"]
            )
        )
    if "kms_key_arn" in value:
        out["KMSKeyArn"] = value["kms_key_arn"]
    if "metrics_config" in value:
        import aws_sdk_lambda.types.event_source_mapping_metrics_config

        out["MetricsConfig"] = (
            aws_sdk_lambda.types.event_source_mapping_metrics_config.serialize_json(
                value["metrics_config"]
            )
        )
    if "logging_config" in value:
        import aws_sdk_lambda.types.event_source_mapping_logging_config

        out["LoggingConfig"] = (
            aws_sdk_lambda.types.event_source_mapping_logging_config.serialize_json(
                value["logging_config"]
            )
        )
    if "provisioned_poller_config" in value:
        import aws_sdk_lambda.types.provisioned_poller_config

        out["ProvisionedPollerConfig"] = (
            aws_sdk_lambda.types.provisioned_poller_config.serialize_json(
                value["provisioned_poller_config"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateEventSourceMappingRequest:
    out: CreateEventSourceMappingRequest = {}  # type: ignore[typeddict-item]
    if "EventSourceArn" in data:
        out["event_source_arn"] = data["EventSourceArn"]
    if "FunctionName" in data:
        out["function_name"] = data["FunctionName"]
    else:
        raise DeserializationError(
            "CreateEventSourceMappingRequest.function_name required"
        )
    if "Enabled" in data:
        out["enabled"] = data["Enabled"]
    if "BatchSize" in data:
        out["batch_size"] = data["BatchSize"]
    if "FilterCriteria" in data:
        import aws_sdk_lambda.types.filter_criteria

        out["filter_criteria"] = aws_sdk_lambda.types.filter_criteria.deserialize_json(
            data["FilterCriteria"]
        )
    if "MaximumBatchingWindowInSeconds" in data:
        out["maximum_batching_window_in_seconds"] = data[
            "MaximumBatchingWindowInSeconds"
        ]
    if "ParallelizationFactor" in data:
        out["parallelization_factor"] = data["ParallelizationFactor"]
    if "StartingPosition" in data:
        import aws_sdk_lambda.types.event_source_position

        out["starting_position"] = (
            aws_sdk_lambda.types.event_source_position.deserialize_json(
                data["StartingPosition"]
            )
        )
    if "StartingPositionTimestamp" in data:
        import aws_sdk_lambda.types.date

        out["starting_position_timestamp"] = aws_sdk_lambda.types.date.deserialize_json(
            data["StartingPositionTimestamp"]
        )
    if "DestinationConfig" in data:
        import aws_sdk_lambda.types.destination_config

        out["destination_config"] = (
            aws_sdk_lambda.types.destination_config.deserialize_json(
                data["DestinationConfig"]
            )
        )
    if "MaximumRecordAgeInSeconds" in data:
        out["maximum_record_age_in_seconds"] = data["MaximumRecordAgeInSeconds"]
    if "BisectBatchOnFunctionError" in data:
        out["bisect_batch_on_function_error"] = data["BisectBatchOnFunctionError"]
    if "MaximumRetryAttempts" in data:
        out["maximum_retry_attempts"] = data["MaximumRetryAttempts"]
    if "Tags" in data:
        import aws_sdk_lambda.types.tags

        out["tags"] = aws_sdk_lambda.types.tags.deserialize_json(data["Tags"])
    if "TumblingWindowInSeconds" in data:
        out["tumbling_window_in_seconds"] = data["TumblingWindowInSeconds"]
    if "Topics" in data:
        import aws_sdk_lambda.types.topics

        out["topics"] = aws_sdk_lambda.types.topics.deserialize_json(data["Topics"])
    if "Queues" in data:
        import aws_sdk_lambda.types.queues

        out["queues"] = aws_sdk_lambda.types.queues.deserialize_json(data["Queues"])
    if "SourceAccessConfigurations" in data:
        import aws_sdk_lambda.types.source_access_configurations

        out["source_access_configurations"] = (
            aws_sdk_lambda.types.source_access_configurations.deserialize_json(
                data["SourceAccessConfigurations"]
            )
        )
    if "SelfManagedEventSource" in data:
        import aws_sdk_lambda.types.self_managed_event_source

        out["self_managed_event_source"] = (
            aws_sdk_lambda.types.self_managed_event_source.deserialize_json(
                data["SelfManagedEventSource"]
            )
        )
    if "FunctionResponseTypes" in data:
        import aws_sdk_lambda.types.function_response_type_list

        out["function_response_types"] = (
            aws_sdk_lambda.types.function_response_type_list.deserialize_json(
                data["FunctionResponseTypes"]
            )
        )
    if "AmazonManagedKafkaEventSourceConfig" in data:
        import aws_sdk_lambda.types.amazon_managed_kafka_event_source_config

        out["amazon_managed_kafka_event_source_config"] = (
            aws_sdk_lambda.types.amazon_managed_kafka_event_source_config.deserialize_json(
                data["AmazonManagedKafkaEventSourceConfig"]
            )
        )
    if "SelfManagedKafkaEventSourceConfig" in data:
        import aws_sdk_lambda.types.self_managed_kafka_event_source_config

        out["self_managed_kafka_event_source_config"] = (
            aws_sdk_lambda.types.self_managed_kafka_event_source_config.deserialize_json(
                data["SelfManagedKafkaEventSourceConfig"]
            )
        )
    if "ScalingConfig" in data:
        import aws_sdk_lambda.types.scaling_config

        out["scaling_config"] = aws_sdk_lambda.types.scaling_config.deserialize_json(
            data["ScalingConfig"]
        )
    if "DocumentDBEventSourceConfig" in data:
        import aws_sdk_lambda.types.document_db_event_source_config

        out["document_db_event_source_config"] = (
            aws_sdk_lambda.types.document_db_event_source_config.deserialize_json(
                data["DocumentDBEventSourceConfig"]
            )
        )
    if "KMSKeyArn" in data:
        out["kms_key_arn"] = data["KMSKeyArn"]
    if "MetricsConfig" in data:
        import aws_sdk_lambda.types.event_source_mapping_metrics_config

        out["metrics_config"] = (
            aws_sdk_lambda.types.event_source_mapping_metrics_config.deserialize_json(
                data["MetricsConfig"]
            )
        )
    if "LoggingConfig" in data:
        import aws_sdk_lambda.types.event_source_mapping_logging_config

        out["logging_config"] = (
            aws_sdk_lambda.types.event_source_mapping_logging_config.deserialize_json(
                data["LoggingConfig"]
            )
        )
    if "ProvisionedPollerConfig" in data:
        import aws_sdk_lambda.types.provisioned_poller_config

        out["provisioned_poller_config"] = (
            aws_sdk_lambda.types.provisioned_poller_config.deserialize_json(
                data["ProvisionedPollerConfig"]
            )
        )
    return out
