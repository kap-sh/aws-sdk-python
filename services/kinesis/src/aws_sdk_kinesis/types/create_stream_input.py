"""Generated from Smithy shape ``com.amazonaws.kinesis#CreateStreamInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.max_record_size_in_ki_b
    import aws_sdk_kinesis.types.natural_integer_object
    import aws_sdk_kinesis.types.positive_integer_object
    import aws_sdk_kinesis.types.stream_mode_details
    import aws_sdk_kinesis.types.stream_name
    import aws_sdk_kinesis.types.tag_map


class CreateStreamInput(TypedDict):
    stream_name: "aws_sdk_kinesis.types.stream_name.StreamName"
    """<p>A name to identify the stream. The stream name is scoped to the Amazon Web Services account used by the application that creates the stream. It is also scoped by Amazon Web Services Region. That is, two streams in two different Amazon Web Services accounts can have the same name. Two streams in the same Amazon Web Services account but in two different Regions can also have the same name.</p>"""
    shard_count: NotRequired[
        "aws_sdk_kinesis.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The number of shards that the stream will use. The throughput of the stream is a function of the number of shards; more shards are required for greater provisioned throughput.</p>"""
    stream_mode_details: NotRequired[
        "aws_sdk_kinesis.types.stream_mode_details.StreamModeDetails"
    ]
    """<p> Indicates the capacity mode of the data stream. Currently, in Kinesis Data Streams, you can choose between an <b>on-demand</b> capacity mode and a <b>provisioned</b> capacity mode for your data streams.</p>"""
    tags: NotRequired["aws_sdk_kinesis.types.tag_map.TagMap"]
    """<p>A set of up to 50 key-value pairs to use to create the tags. A tag consists of a required key and an optional value.</p>"""
    warm_throughput_mi_bps: NotRequired[
        "aws_sdk_kinesis.types.natural_integer_object.NaturalIntegerObject"
    ]
    """<p>The target warm throughput in MB/s that the stream should be scaled to handle. This represents the throughput capacity that will be immediately available for write operations.</p>"""
    max_record_size_in_ki_b: NotRequired[
        "aws_sdk_kinesis.types.max_record_size_in_ki_b.MaxRecordSizeInKiB"
    ]
    """<p>The maximum record size of a single record in kibibyte (KiB) that you can write to, and read from a stream.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateStreamInput) -> dict:
    out: dict = {}
    out["StreamName"] = value["stream_name"]
    if "shard_count" in value:
        out["ShardCount"] = value["shard_count"]
    if "stream_mode_details" in value:
        import aws_sdk_kinesis.types.stream_mode_details

        out["StreamModeDetails"] = (
            aws_sdk_kinesis.types.stream_mode_details.serialize_aws_json_1_1(
                value["stream_mode_details"]
            )
        )
    if "tags" in value:
        import aws_sdk_kinesis.types.tag_map

        out["Tags"] = aws_sdk_kinesis.types.tag_map.serialize_aws_json_1_1(
            value["tags"]
        )
    if "warm_throughput_mi_bps" in value:
        out["WarmThroughputMiBps"] = value["warm_throughput_mi_bps"]
    if "max_record_size_in_ki_b" in value:
        out["MaxRecordSizeInKiB"] = value["max_record_size_in_ki_b"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateStreamInput:
    out: CreateStreamInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    else:
        raise DeserializationError("CreateStreamInput.stream_name required")
    if "ShardCount" in data:
        out["shard_count"] = data["ShardCount"]
    if "StreamModeDetails" in data:
        import aws_sdk_kinesis.types.stream_mode_details

        out["stream_mode_details"] = (
            aws_sdk_kinesis.types.stream_mode_details.deserialize_aws_json_1_1(
                data["StreamModeDetails"]
            )
        )
    if "Tags" in data:
        import aws_sdk_kinesis.types.tag_map

        out["tags"] = aws_sdk_kinesis.types.tag_map.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if "WarmThroughputMiBps" in data:
        out["warm_throughput_mi_bps"] = data["WarmThroughputMiBps"]
    if "MaxRecordSizeInKiB" in data:
        out["max_record_size_in_ki_b"] = data["MaxRecordSizeInKiB"]
    return out
