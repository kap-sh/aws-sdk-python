"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordInput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.data
    import aws_sdk_kinesis.types.hash_key
    import aws_sdk_kinesis.types.partition_key
    import aws_sdk_kinesis.types.sequence_number
    import aws_sdk_kinesis.types.stream_arn
    import aws_sdk_kinesis.types.stream_id
    import aws_sdk_kinesis.types.stream_name


class PutRecordInput(TypedDict):
    stream_name: NotRequired["aws_sdk_kinesis.types.stream_name.StreamName"]
    """<p>The name of the stream to put the data record into.</p>"""
    data: "aws_sdk_kinesis.types.data.Data"
    """<p>The data blob to put into the record, which is base64-encoded when the blob is serialized. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (10 MiB).</p>"""
    partition_key: "aws_sdk_kinesis.types.partition_key.PartitionKey"
    """<p>Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.</p>"""
    explicit_hash_key: NotRequired["aws_sdk_kinesis.types.hash_key.HashKey"]
    """<p>The hash value used to explicitly determine the shard the data record is assigned to by overriding the partition key hash.</p>"""
    sequence_number_for_ordering: NotRequired[
        "aws_sdk_kinesis.types.sequence_number.SequenceNumber"
    ]
    """<p>Guarantees strictly increasing sequence numbers, for puts from the same client and to the same partition key. Usage: set the <code>SequenceNumberForOrdering</code> of record <i>n</i> to the sequence number of record <i>n-1</i> (as returned in the result when putting record <i>n-1</i>). If this parameter is not set, records are coarsely ordered based on arrival time.</p>"""
    stream_arn: NotRequired["aws_sdk_kinesis.types.stream_arn.StreamARN"]
    """<p>The ARN of the stream.</p>"""
    stream_id: NotRequired["aws_sdk_kinesis.types.stream_id.StreamId"]
    """<p>Not Implemented. Reserved for future use.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordInput) -> dict:
    out: dict = {}
    if "stream_name" in value:
        out["StreamName"] = value["stream_name"]
    import aws_sdk_kinesis.types.data

    out["Data"] = aws_sdk_kinesis.types.data.serialize_aws_json_1_1(value["data"])
    out["PartitionKey"] = value["partition_key"]
    if "explicit_hash_key" in value:
        out["ExplicitHashKey"] = value["explicit_hash_key"]
    if "sequence_number_for_ordering" in value:
        out["SequenceNumberForOrdering"] = value["sequence_number_for_ordering"]
    if "stream_arn" in value:
        out["StreamARN"] = value["stream_arn"]
    if "stream_id" in value:
        out["StreamId"] = value["stream_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordInput:
    out: PutRecordInput = {}  # type: ignore[typeddict-item]
    if "StreamName" in data:
        out["stream_name"] = data["StreamName"]
    if "Data" in data:
        import aws_sdk_kinesis.types.data

        out["data"] = aws_sdk_kinesis.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        raise DeserializationError("PutRecordInput.data required")
    if "PartitionKey" in data:
        out["partition_key"] = data["PartitionKey"]
    else:
        raise DeserializationError("PutRecordInput.partition_key required")
    if "ExplicitHashKey" in data:
        out["explicit_hash_key"] = data["ExplicitHashKey"]
    if "SequenceNumberForOrdering" in data:
        out["sequence_number_for_ordering"] = data["SequenceNumberForOrdering"]
    if "StreamARN" in data:
        out["stream_arn"] = data["StreamARN"]
    if "StreamId" in data:
        out["stream_id"] = data["StreamId"]
    return out
