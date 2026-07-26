"""Generated from Smithy shape ``com.amazonaws.glue#KinesisStreamingSourceOptions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.boxed_boolean
    import capo_glue.types.boxed_non_negative_int
    import capo_glue.types.boxed_non_negative_long
    import capo_glue.types.enclosed_in_string_property
    import capo_glue.types.iso8601_date_time
    import capo_glue.types.starting_position


class KinesisStreamingSourceOptions(TypedDict, closed=True):
    endpoint_url: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The URL of the Kinesis endpoint.</p>"""
    stream_name: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The name of the Kinesis data stream.</p>"""
    classification: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>An optional classification.</p>"""
    delimiter: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>Specifies the delimiter character.</p>"""
    starting_position: NotRequired["capo_glue.types.starting_position.StartingPosition"]
    r"""<p>The starting position in the Kinesis data stream to read data from. The possible values are <code>\"latest\"</code>, <code>\"trim_horizon\"</code>, <code>\"earliest\"</code>, or a timestamp string in UTC format in the pattern <code>yyyy-mm-ddTHH:MM:SSZ</code> (where <code>Z</code> represents a UTC timezone offset with a +/-. For example: \"2023-04-04T08:00:00-04:00\"). The default value is <code>\"latest\"</code>.</p> <p>Note: Using a value that is a timestamp string in UTC format for \"startingPosition\" is supported only for Glue version 4.0 or later.</p>"""
    max_fetch_time_in_ms: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The maximum time spent for the job executor to read records for the current batch from the Kinesis data stream, specified in milliseconds (ms). Multiple <code>GetRecords</code> API calls may be made within this time. The default value is <code>1000</code>.</p>"""
    max_fetch_records_per_shard: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The maximum number of records to fetch per shard in the Kinesis data stream per microbatch. Note: The client can exceed this limit if the streaming job has already read extra records from Kinesis (in the same get-records call). If <code>MaxFetchRecordsPerShard</code> needs to be strict then it needs to be a multiple of <code>MaxRecordPerRead</code>. The default value is <code>100000</code>.</p>"""
    max_record_per_read: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The maximum number of records to fetch from the Kinesis data stream in each getRecords operation. The default value is <code>10000</code>.</p>"""
    add_idle_time_between_reads: NotRequired[
        "capo_glue.types.boxed_boolean.BoxedBoolean"
    ]
    r"""<p>Adds a time delay between two consecutive getRecords operations. The default value is <code>\"False\"</code>. This option is only configurable for Glue version 2.0 and above.</p>"""
    idle_time_between_reads_in_ms: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The minimum time delay between two consecutive getRecords operations, specified in ms. The default value is <code>1000</code>. This option is only configurable for Glue version 2.0 and above.</p>"""
    describe_shard_interval: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The minimum time interval between two ListShards API calls for your script to consider resharding. The default value is <code>1s</code>.</p>"""
    num_retries: NotRequired[
        "capo_glue.types.boxed_non_negative_int.BoxedNonNegativeInt"
    ]
    """<p>The maximum number of retries for Kinesis Data Streams API requests. The default value is <code>3</code>.</p>"""
    retry_interval_ms: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The cool-off time period (specified in ms) before retrying the Kinesis Data Streams API call. The default value is <code>1000</code>.</p>"""
    max_retry_interval_ms: NotRequired[
        "capo_glue.types.boxed_non_negative_long.BoxedNonNegativeLong"
    ]
    """<p>The maximum cool-off time period (specified in ms) between two retries of a Kinesis Data Streams API call. The default value is <code>10000</code>.</p>"""
    avoid_empty_batches: NotRequired["capo_glue.types.boxed_boolean.BoxedBoolean"]
    r"""<p>Avoids creating an empty microbatch job by checking for unread data in the Kinesis data stream before the batch is started. The default value is <code>\"False\"</code>.</p>"""
    stream_arn: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon Resource Name (ARN) of the Kinesis data stream.</p>"""
    role_arn: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>The Amazon Resource Name (ARN) of the role to assume using AWS Security Token Service (AWS STS). This role must have permissions for describe or read record operations for the Kinesis data stream. You must use this parameter when accessing a data stream in a different account. Used in conjunction with <code>\"awsSTSSessionName\"</code>.</p>"""
    role_session_name: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>An identifier for the session assuming the role using AWS STS. You must use this parameter when accessing a data stream in a different account. Used in conjunction with <code>\"awsSTSRoleARN\"</code>.</p>"""
    add_record_timestamp: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>When this option is set to 'true', the data output will contain an additional column named \"__src_timestamp\" that indicates the time when the corresponding record received by the stream. The default value is 'false'. This option is supported in Glue version 4.0 or later.</p>"""
    emit_consumer_lag_metrics: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    r"""<p>When this option is set to 'true', for each batch, it will emit the metrics for the duration between the oldest record received by the stream and the time it arrives in Glue to CloudWatch. The metric's name is \"glue.driver.streaming.maxConsumerLagInMs\". The default value is 'false'. This option is supported in Glue version 4.0 or later.</p>"""
    starting_timestamp: NotRequired["capo_glue.types.iso8601_date_time.Iso8601DateTime"]
    r"""<p>The timestamp of the record in the Kinesis data stream to start reading data from. The possible values are a timestamp string in UTC format of the pattern <code>yyyy-mm-ddTHH:MM:SSZ</code> (where Z represents a UTC timezone offset with a +/-. For example: \"2023-04-04T08:00:00+08:00\"). </p>"""
    fanout_consumer_arn: NotRequired[
        "capo_glue.types.enclosed_in_string_property.EnclosedInStringProperty"
    ]
    """<p>The Amazon Resource Name (ARN) of the Kinesis Data Streams enhanced fan-out consumer. When specified, enables enhanced fan-out for dedicated throughput and lower latency data consumption.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KinesisStreamingSourceOptions) -> dict:
    out: dict = {}
    if "endpoint_url" in value:
        out["EndpointUrl"] = value["endpoint_url"]
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    if "classification" in value:
        out["Classification"] = value["classification"]
    if "delimiter" in value:
        out["Delimiter"] = value["delimiter"]
    if "starting_position" in value:
        import capo_glue.types.starting_position

        out["StartingPosition"] = (
            capo_glue.types.starting_position.serialize_aws_json_1_1(
                value["starting_position"]
            )
        )
    if "max_fetch_time_in_ms" in value:
        out["MaxFetchTimeInMs"] = value["max_fetch_time_in_ms"]
    if "max_fetch_records_per_shard" in value:
        out["MaxFetchRecordsPerShard"] = value["max_fetch_records_per_shard"]
    if "max_record_per_read" in value:
        out["MaxRecordPerRead"] = value["max_record_per_read"]
    if "add_idle_time_between_reads" in value:
        out["AddIdleTimeBetweenReads"] = value["add_idle_time_between_reads"]
    if "idle_time_between_reads_in_ms" in value:
        out["IdleTimeBetweenReadsInMs"] = value["idle_time_between_reads_in_ms"]
    if "describe_shard_interval" in value:
        out["DescribeShardInterval"] = value["describe_shard_interval"]
    if "num_retries" in value:
        out["NumRetries"] = value["num_retries"]
    if "retry_interval_ms" in value:
        out["RetryIntervalMs"] = value["retry_interval_ms"]
    if "max_retry_interval_ms" in value:
        out["MaxRetryIntervalMs"] = value["max_retry_interval_ms"]
    if "avoid_empty_batches" in value:
        out["AvoidEmptyBatches"] = value["avoid_empty_batches"]
    if "stream_arn" in value:
        out["StreamArn"] = value["stream_arn"]
    if "role_arn" in value:
        out["RoleArn"] = value["role_arn"]
    if "role_session_name" in value:
        out["RoleSessionName"] = value["role_session_name"]
    if "add_record_timestamp" in value:
        out["AddRecordTimestamp"] = value["add_record_timestamp"]
    if "emit_consumer_lag_metrics" in value:
        out["EmitConsumerLagMetrics"] = value["emit_consumer_lag_metrics"]
    if "starting_timestamp" in value:
        import capo_glue.types.iso8601_date_time

        out["StartingTimestamp"] = (
            capo_glue.types.iso8601_date_time.serialize_aws_json_1_1(
                value["starting_timestamp"]
            )
        )
    if "fanout_consumer_arn" in value:
        out["FanoutConsumerARN"] = value["fanout_consumer_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KinesisStreamingSourceOptions:
    out: KinesisStreamingSourceOptions = {}  # type: ignore[typeddict-item]
    if "EndpointUrl" in data:
        out["endpoint_url"] = data["EndpointUrl"]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "Classification" in data:
        out["classification"] = data["Classification"]
    if "Delimiter" in data:
        out["delimiter"] = data["Delimiter"]
    if "StartingPosition" in data:
        import capo_glue.types.starting_position

        out["starting_position"] = (
            capo_glue.types.starting_position.deserialize_aws_json_1_1(
                data["StartingPosition"]
            )
        )
    if "MaxFetchTimeInMs" in data:
        out["max_fetch_time_in_ms"] = data["MaxFetchTimeInMs"]
    if "MaxFetchRecordsPerShard" in data:
        out["max_fetch_records_per_shard"] = data["MaxFetchRecordsPerShard"]
    if "MaxRecordPerRead" in data:
        out["max_record_per_read"] = data["MaxRecordPerRead"]
    if "AddIdleTimeBetweenReads" in data:
        out["add_idle_time_between_reads"] = data["AddIdleTimeBetweenReads"]
    if "IdleTimeBetweenReadsInMs" in data:
        out["idle_time_between_reads_in_ms"] = data["IdleTimeBetweenReadsInMs"]
    if "DescribeShardInterval" in data:
        out["describe_shard_interval"] = data["DescribeShardInterval"]
    if "NumRetries" in data:
        out["num_retries"] = data["NumRetries"]
    if "RetryIntervalMs" in data:
        out["retry_interval_ms"] = data["RetryIntervalMs"]
    if "MaxRetryIntervalMs" in data:
        out["max_retry_interval_ms"] = data["MaxRetryIntervalMs"]
    if "AvoidEmptyBatches" in data:
        out["avoid_empty_batches"] = data["AvoidEmptyBatches"]
    if "StreamArn" in data:
        out["stream_arn"] = data["StreamArn"]
    if "RoleArn" in data:
        out["role_arn"] = data["RoleArn"]
    if "RoleSessionName" in data:
        out["role_session_name"] = data["RoleSessionName"]
    if "AddRecordTimestamp" in data:
        out["add_record_timestamp"] = data["AddRecordTimestamp"]
    if "EmitConsumerLagMetrics" in data:
        out["emit_consumer_lag_metrics"] = data["EmitConsumerLagMetrics"]
    if "StartingTimestamp" in data:
        import capo_glue.types.iso8601_date_time

        out["starting_timestamp"] = (
            capo_glue.types.iso8601_date_time.deserialize_aws_json_1_1(
                data["StartingTimestamp"]
            )
        )
    if "FanoutConsumerARN" in data:
        out["fanout_consumer_arn"] = data["FanoutConsumerARN"]
    return out
