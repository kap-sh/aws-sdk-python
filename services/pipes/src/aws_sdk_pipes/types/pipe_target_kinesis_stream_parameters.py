"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetKinesisStreamParameters``."""

from typing import TYPE_CHECKING, TypedDict

from aws_sdk_pipes.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_pipes.types.kinesis_partition_key


class PipeTargetKinesisStreamParameters(TypedDict):
    partition_key: "aws_sdk_pipes.types.kinesis_partition_key.KinesisPartitionKey"
    """<p>Determines which shard in the stream the data record is assigned to. Partition keys are Unicode strings with a maximum length limit of 256 characters for each key. Amazon Kinesis Data Streams uses the partition key as input to a hash function that maps the partition key and associated data to a specific shard. Specifically, an MD5 hash function is used to map partition keys to 128-bit integer values and to map associated data records to shards. As a result of this hashing mechanism, all data records with the same partition key map to the same shard within the stream.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetKinesisStreamParameters) -> dict:
    out: dict = {}
    out["PartitionKey"] = value["partition_key"]
    return out


def deserialize_json(data: dict) -> PipeTargetKinesisStreamParameters:
    out: PipeTargetKinesisStreamParameters = {}  # type: ignore[typeddict-item]
    if "PartitionKey" in data:
        out["partition_key"] = data["PartitionKey"]
    else:
        raise DeserializationError(
            "PipeTargetKinesisStreamParameters.partition_key required"
        )
    return out
