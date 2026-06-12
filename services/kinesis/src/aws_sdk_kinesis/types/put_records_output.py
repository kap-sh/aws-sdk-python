"""Generated from Smithy shape ``com.amazonaws.kinesis#PutRecordsOutput``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_kinesis.errors import DeserializationError

if TYPE_CHECKING:
    import aws_sdk_kinesis.types.encryption_type
    import aws_sdk_kinesis.types.positive_integer_object
    import aws_sdk_kinesis.types.put_records_result_entry_list


class PutRecordsOutput(TypedDict):
    failed_record_count: NotRequired[
        "aws_sdk_kinesis.types.positive_integer_object.PositiveIntegerObject"
    ]
    """<p>The number of unsuccessfully processed records in a <code>PutRecords</code> request.</p>"""
    records: (
        "aws_sdk_kinesis.types.put_records_result_entry_list.PutRecordsResultEntryList"
    )
    """<p>An array of successfully and unsuccessfully processed record results. A record that is successfully added to a stream includes <code>SequenceNumber</code> and <code>ShardId</code> in the result. A record that fails to be added to a stream includes <code>ErrorCode</code> and <code>ErrorMessage</code> in the result.</p>"""
    encryption_type: NotRequired["aws_sdk_kinesis.types.encryption_type.EncryptionType"]
    """<p>The encryption type used on the records. This parameter can be one of the following values:</p> <ul> <li> <p> <code>NONE</code>: Do not encrypt the records.</p> </li> <li> <p> <code>KMS</code>: Use server-side encryption on the records using a customer-managed Amazon Web Services KMS key.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutRecordsOutput) -> dict:
    out: dict = {}
    if "failed_record_count" in value:
        out["FailedRecordCount"] = value["failed_record_count"]
    import aws_sdk_kinesis.types.put_records_result_entry_list

    out["Records"] = (
        aws_sdk_kinesis.types.put_records_result_entry_list.serialize_aws_json_1_1(
            value["records"]
        )
    )
    if "encryption_type" in value:
        import aws_sdk_kinesis.types.encryption_type

        out["EncryptionType"] = (
            aws_sdk_kinesis.types.encryption_type.serialize_aws_json_1_1(
                value["encryption_type"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutRecordsOutput:
    out: PutRecordsOutput = {}  # type: ignore[typeddict-item]
    if "FailedRecordCount" in data:
        out["failed_record_count"] = data["FailedRecordCount"]
    if "Records" in data:
        import aws_sdk_kinesis.types.put_records_result_entry_list

        out["records"] = (
            aws_sdk_kinesis.types.put_records_result_entry_list.deserialize_aws_json_1_1(
                data["Records"]
            )
        )
    else:
        raise DeserializationError("PutRecordsOutput.records required")
    if "EncryptionType" in data:
        import aws_sdk_kinesis.types.encryption_type

        out["encryption_type"] = (
            aws_sdk_kinesis.types.encryption_type.deserialize_aws_json_1_1(
                data["EncryptionType"]
            )
        )
    return out
