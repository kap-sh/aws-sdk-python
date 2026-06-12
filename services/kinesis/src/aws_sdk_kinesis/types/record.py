"""Generated from Smithy shape ``com.amazonaws.kinesis#Record``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.data
    import aws_sdk_kinesis.types.encryption_type
    import aws_sdk_kinesis.types.partition_key
    import aws_sdk_kinesis.types.sequence_number
    import aws_sdk_kinesis.types.timestamp


class Record(TypedDict):
    sequence_number: "aws_sdk_kinesis.types.sequence_number.SequenceNumber"
    """<p>The unique identifier of the record within its shard.</p>"""
    approximate_arrival_timestamp: NotRequired[
        "aws_sdk_kinesis.types.timestamp.Timestamp"
    ]
    """<p>The approximate time that the record was inserted into the stream.</p>"""
    data: "aws_sdk_kinesis.types.data.Data"
    """<p>The data blob. The data in the blob is both opaque and immutable to Kinesis Data Streams, which does not inspect, interpret, or change the data in the blob in any way. When the data blob (the payload before base64-encoding) is added to the partition key size, the total size must not exceed the maximum record size (1 MiB).</p>"""
    partition_key: "aws_sdk_kinesis.types.partition_key.PartitionKey"
    """<p>Identifies which shard in the stream the data record is assigned to.</p>"""
    encryption_type: NotRequired["aws_sdk_kinesis.types.encryption_type.EncryptionType"]
    """<p>The encryption type used on the record. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records in the stream.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records in the stream using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Record) -> dict:
    out: dict = {}
    out["SequenceNumber"] = value["sequence_number"]
    if "approximate_arrival_timestamp" in value:
        import aws_sdk_kinesis.types.timestamp

        out["ApproximateArrivalTimestamp"] = (
            aws_sdk_kinesis.types.timestamp.serialize_aws_json_1_1(
                value["approximate_arrival_timestamp"]
            )
        )
    import aws_sdk_kinesis.types.data

    out["Data"] = aws_sdk_kinesis.types.data.serialize_aws_json_1_1(value["data"])
    out["PartitionKey"] = value["partition_key"]
    if "encryption_type" in value:
        import aws_sdk_kinesis.types.encryption_type

        out["EncryptionType"] = (
            aws_sdk_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Record:
    out: Record = {}  # type: ignore[typeddict-item]
    if "SequenceNumber" in data:
        out["sequence_number"] = data["SequenceNumber"]
    else:
        raise DeserializationError("Record.sequence_number required")
    if "ApproximateArrivalTimestamp" in data:
        import aws_sdk_kinesis.types.timestamp

        out["approximate_arrival_timestamp"] = (
            aws_sdk_kinesis.types.timestamp.deserialize_aws_json_1_1(
                data["ApproximateArrivalTimestamp"]
            )
        )
    if "Data" in data:
        import aws_sdk_kinesis.types.data

        out["data"] = aws_sdk_kinesis.types.data.deserialize_aws_json_1_1(data["Data"])
    else:
        raise DeserializationError("Record.data required")
    if "PartitionKey" in data:
        out["partition_key"] = data["PartitionKey"]
    else:
        raise DeserializationError("Record.partition_key required")
    if "EncryptionType" in data:
        import aws_sdk_kinesis.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    return out
