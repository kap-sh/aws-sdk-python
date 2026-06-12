"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.encryption_type
    import aws_sdk_kinesis.types.sequence_number
    import aws_sdk_kinesis.types.shard_id


class PutRecordOutput(TypedDict):
    shard_id: "aws_sdk_kinesis.types.shard_id.ShardId"
    """<p>The shard ID of the shard where the data record was placed.</p>"""
    sequence_number: "aws_sdk_kinesis.types.sequence_number.SequenceNumber"
    """<p>The sequence number identifier that was assigned to the put data record. The sequence number for the record is unique across all records in the stream. A sequence number is the identifier associated with every record put into the stream.</p>"""
    encryption_type: NotRequired["aws_sdk_kinesis.types.encryption_type.EncryptionType"]
    """<p>The encryption type to use on the record. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records in the stream.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordOutput) -> dict:
    out: dict = {}
    out["ShardId"] = value["shard_id"]
    out["SequenceNumber"] = value["sequence_number"]
    if "encryption_type" in value:
        import aws_sdk_kinesis.types.encryption_type

        out["EncryptionType"] = (
            aws_sdk_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordOutput:
    out: PutRecordOutput = {}  # type: ignore[typeddict-item]
    if "ShardId" in data:
        out["shard_id"] = data["ShardId"]
    else:
        raise DeserializationError("PutRecordOutput.shard_id required")
    if "SequenceNumber" in data:
        out["sequence_number"] = data["SequenceNumber"]
    else:
        raise DeserializationError("PutRecordOutput.sequence_number required")
    if "EncryptionType" in data:
        import aws_sdk_kinesis.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    return out
