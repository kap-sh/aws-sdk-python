"""Generated from Smithy shape ``com.amazonaws.rds#StopActivityStreamResponse``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

from aws_sdk_rds._protocol.xml import Element

if TYPE_CHECKING:
    import aws_sdk_rds.types.activity_stream_status
    import aws_sdk_rds.types.string


class StopActivityStreamResponse(TypedDict):
    kms_key_id: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The Amazon Web Services KMS key identifier used for encrypting messages in the database activity stream.</p> <p>The Amazon Web Services KMS key identifier is the key ARN, key ID, alias ARN, or alias name for the KMS key.</p>"""
    kinesis_stream_name: NotRequired["aws_sdk_rds.types.string.String"]
    """<p>The name of the Amazon Kinesis data stream used for the database activity stream.</p>"""
    status: NotRequired["aws_sdk_rds.types.activity_stream_status.ActivityStreamStatus"]
    """<p>The status of the database activity stream.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: StopActivityStreamResponse, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if "kms_key_id" in value:
        pairs.append((f"{prefix}.KmsKeyId", str(value["kms_key_id"])))
    if "kinesis_stream_name" in value:
        pairs.append((f"{prefix}.KinesisStreamName", str(value["kinesis_stream_name"])))
    if "status" in value:
        import aws_sdk_rds.types.activity_stream_status

        aws_sdk_rds.types.activity_stream_status.serialize_query(
            value["status"], pairs, f"{prefix}.Status"
        )


def deserialize_query(el: Element) -> StopActivityStreamResponse:
    out: StopActivityStreamResponse = {}  # type: ignore[typeddict-item]
    child_kms_key_id = el.find("KmsKeyId")
    if child_kms_key_id is not None:
        out["kms_key_id"] = str(child_kms_key_id.text or "")
    child_kinesis_stream_name = el.find("KinesisStreamName")
    if child_kinesis_stream_name is not None:
        out["kinesis_stream_name"] = str(child_kinesis_stream_name.text or "")
    child_status = el.find("Status")
    if child_status is not None:
        import aws_sdk_rds.types.activity_stream_status

        out["status"] = aws_sdk_rds.types.activity_stream_status.deserialize_query(
            child_status
        )
    return out
