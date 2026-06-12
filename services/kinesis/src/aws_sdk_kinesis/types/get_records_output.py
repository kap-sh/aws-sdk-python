"""Generated from Smithy shape ``com.amazonaws.kinesis#GetRecordsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.child_shard_list
    import aws_sdk_kinesis.types.millis_behind_latest
    import aws_sdk_kinesis.types.record_list
    import aws_sdk_kinesis.types.shard_iterator


class GetRecordsOutput(TypedDict):
    records: "aws_sdk_kinesis.types.record_list.RecordList"
    """<p>The data records retrieved from the shard.</p>"""
    next_shard_iterator: NotRequired[
        "aws_sdk_kinesis.types.shard_iterator.ShardIterator"
    ]
    """<p>The next position in the shard from which to start sequentially reading data records. If set to <code>null</code>, the shard has been closed and the requested iterator does not return any more data. </p>"""
    millis_behind_latest: NotRequired[
        "aws_sdk_kinesis.types.millis_behind_latest.MillisBehindLatest"
    ]
    """<p>The number of milliseconds the <a>GetRecords</a> response is from the tip of the stream, indicating how far behind current time the consumer is. A value of zero indicates that record processing is caught up, and there are no new records to process at this moment.</p>"""
    child_shards: NotRequired["aws_sdk_kinesis.types.child_shard_list.ChildShardList"]
    """<p>The list of the current shard's child shards, returned in the <code>GetRecords</code> API's response only when the end of the current shard is reached.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetRecordsOutput) -> dict:
    out: dict = {}
    import aws_sdk_kinesis.types.record_list

    out["Records"] = aws_sdk_kinesis.types.record_list.serialize_aws_json_1_1(
        value["records"]
    )
    if "next_shard_iterator" in value:
        out["NextShardIterator"] = value["next_shard_iterator"]
    if "millis_behind_latest" in value:
        out["MillisBehindLatest"] = value["millis_behind_latest"]
    if "child_shards" in value:
        import aws_sdk_kinesis.types.child_shard_list

        out["ChildShards"] = (
            aws_sdk_kinesis.types.child_shard_list.serialize_aws_json_1_1(
                value["child_shards"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetRecordsOutput:
    out: GetRecordsOutput = {}  # type: ignore[typeddict-item]
    if "Records" in data:
        import aws_sdk_kinesis.types.record_list

        out["records"] = aws_sdk_kinesis.types.record_list.deserialize_aws_json_1_1(
            data["Records"]
        )
    else:
        raise DeserializationError("GetRecordsOutput.records required")
    if "NextShardIterator" in data:
        out["next_shard_iterator"] = data["NextShardIterator"]
    if "MillisBehindLatest" in data:
        out["millis_behind_latest"] = data["MillisBehindLatest"]
    if "ChildShards" in data:
        import aws_sdk_kinesis.types.child_shard_list

        out["child_shards"] = (
            aws_sdk_kinesis.types.child_shard_list.deserialize_aws_json_1_1(
                data["ChildShards"]
            )
        )
    return out
