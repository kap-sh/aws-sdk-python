"""Generated from Smithy shape ``com.amazonaws.kinesis#GetShardIteratorInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis.types.sequence_number
    import capo_kinesis.types.shard_id
    import capo_kinesis.types.shard_iterator_type
    import capo_kinesis.types.stream_arn
    import capo_kinesis.types.stream_id
    import capo_kinesis.types.stream_name
    import capo_kinesis.types.timestamp


class GetShardIteratorInput(TypedDict, closed=True):
    stream_name: NotRequired["capo_kinesis.types.stream_name.StreamName"]
    """<p>The name of the Amazon Kinesis data stream.</p>"""
    shard_id: "capo_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the Kinesis Data Streams shard to get the iterator for.</p>"""
    shard_iterator_type: "capo_kinesis.types.shard_iterator_type.ShardIteratorType"
    """<p>Determines how the shard iterator is used to start reading data records from the shard.</p> <p>The following are the valid Amazon Kinesis shard iterator types:</p> <ul> <li> <p>AT_SEQUENCE_NUMBER - Start reading from the position denoted by a specific sequence number, provided in the value <code>StartingSequenceNumber</code>.</p> </li> <li> <p>AFTER_SEQUENCE_NUMBER - Start reading right after the position denoted by a specific sequence number, provided in the value <code>StartingSequenceNumber</code>.</p> </li> <li> <p>AT_TIMESTAMP - Start reading from the position denoted by a specific time stamp, provided in the value <code>Timestamp</code>.</p> </li> <li> <p>TRIM_HORIZON - Start reading at the last untrimmed record in the shard in the system, which is the oldest data record in the shard.</p> </li> <li> <p>LATEST - Start reading just after the most recent record in the shard, so that you always read the most recent data in the shard.</p> </li> </ul>"""
    starting_sequence_number: NotRequired[
        "capo_kinesis.types.sequence_number.SequenceNumber"
    ]
    """<p>The sequence number of the data record in the shard from which to start reading. Used with shard iterator type AT_SEQUENCE_NUMBER and AFTER_SEQUENCE_NUMBER.</p>"""
    timestamp: NotRequired["capo_kinesis.types.timestamp.Timestamp"]
    """<p>The time stamp of the data record from which to start reading. Used with shard iterator type AT_TIMESTAMP. A time stamp is the Unix epoch date with precision in milliseconds. For example, <code>2016-04-04T19:58:46.480-00:00</code> or <code>1459799926.480</code>. If a record with this exact time stamp does not exist, the iterator returned is for the next (later) record. If the time stamp is older than the current trim horizon, the iterator returned is for the oldest untrimmed data record (TRIM_HORIZON).</p>"""
    stream_arn: NotRequired["capo_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["capo_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetShardIteratorInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    out["ShardId"] = value["shard_id"]
    import capo_kinesis.types.shard_iterator_type

    out["ShardIteratorType"] = (
        capo_kinesis.types.shard_iterator_type.serialize_aws_json_1_1(
            value["shard_iterator_type"]
        )
    )
    if "starting_sequence_number" in value:
        out["StartingSequenceNumber"] = value["starting_sequence_number"]
    if "timestamp" in value:
        import capo_kinesis.types.timestamp

        out["Timestamp"] = capo_kinesis.types.timestamp.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetShardIteratorInput:
    out: GetShardIteratorInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "ShardId" in data:
        out["shard_id"] = data["ShardId"]
    else:
        raise DeserializationError("GetShardIteratorInput.shard_id required")
    if "ShardIteratorType" in data:
        import capo_kinesis.types.shard_iterator_type

        out["shard_iterator_type"] = (
            capo_kinesis.types.shard_iterator_type.deserialize_aws_json_1_1(
                data["ShardIteratorType"]
            )
        )
    else:
        raise DeserializationError("GetShardIteratorInput.shard_iterator_type required")
    if "StartingSequenceNumber" in data:
        out["starting_sequence_number"] = data["StartingSequenceNumber"]
    if "Timestamp" in data:
        import capo_kinesis.types.timestamp

        out["timestamp"] = capo_kinesis.types.timestamp.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
