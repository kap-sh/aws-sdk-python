"""Generated from Smithy shape ``com.amazonaws.firehose#DeliveryStreamEncryptionConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_firehose.types.awskms_key_arn
    import aws_sdk_firehose.types.delivery_stream_encryption_status
    import aws_sdk_firehose.types.failure_description
    import aws_sdk_firehose.types.key_type


class DeliveryStreamEncryptionConfiguration(TypedDict):
    key_arn: NotRequired["aws_sdk_firehose.types.awskms_key_arn.AWSKMSKeyARN"]
    """<p>If <code>KeyType</code> is <code>CUSTOMER_MANAGED_CMK</code>, this field contains the ARN of the customer managed CMK. If <code>KeyType</code> is <code>Amazon Web Services_OWNED_CMK</code>, <code>DeliveryStreamEncryptionConfiguration</code> doesn't contain a value for <code>KeyARN</code>.</p>"""
    key_type: NotRequired["aws_sdk_firehose.types.key_type.KeyType"]
    r"""<p>Indicates the type of customer master key (CMK) that is used for encryption. The default setting is <code>Amazon Web Services_OWNED_CMK</code>. For more information about CMKs, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys\">Customer Master Keys (CMKs)</a>.</p>"""
    status: NotRequired[
        "aws_sdk_firehose.types.delivery_stream_encryption_status.DeliveryStreamEncryptionStatus"
    ]
    """<p>This is the server-side encryption (SSE) status for the Firehose stream. For a full description of the different values of this status, see <a>StartDeliveryStreamEncryption</a> and <a>StopDeliveryStreamEncryption</a>. If this status is <code>ENABLING_FAILED</code> or <code>DISABLING_FAILED</code>, it is the status of the most recent attempt to enable or disable SSE, respectively.</p>"""
    failure_description: NotRequired[
        "aws_sdk_firehose.types.failure_description.FailureDescription"
    ]
    """<p>Provides details in case one of the following operations fails due to an error related to KMS: <a>CreateDeliveryStream</a>, <a>DeleteDeliveryStream</a>, <a>StartDeliveryStreamEncryption</a>, <a>StopDeliveryStreamEncryption</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeliveryStreamEncryptionConfiguration) -> dict:
    out: dict = {}
    if "key_arn" in value:
        out["KeyARN"] = value["key_arn"]
    if "key_type" in value:
        import aws_sdk_firehose.types.key_type

        out["KeyType"] = aws_sdk_firehose.types.key_type.serialize_aws_json_1_1(
            value["key_type"]
        )
    if "status" in value:
        import aws_sdk_firehose.types.delivery_stream_encryption_status

        out["Status"] = (
            aws_sdk_firehose.types.delivery_stream_encryption_status.serialize_aws_json_1_1(
                value["status"]
            )
        )
    if "failure_description" in value:
        import aws_sdk_firehose.types.failure_description

        out["FailureDescription"] = (
            aws_sdk_firehose.types.failure_description.serialize_aws_json_1_1(
                value["failure_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DeliveryStreamEncryptionConfiguration:
    out: DeliveryStreamEncryptionConfiguration = {}  # type: ignore[typeddict-item]
    if "KeyARN" in data:
        out["key_arn"] = data["KeyARN"]
    if "KeyType" in data:
        import aws_sdk_firehose.types.key_type

        out["key_type"] = aws_sdk_firehose.types.key_type.deserialize_aws_json_1_1(
            data["KeyType"]
        )
    if "Status" in data:
        import aws_sdk_firehose.types.delivery_stream_encryption_status

        out["status"] = (
            aws_sdk_firehose.types.delivery_stream_encryption_status.deserialize_aws_json_1_1(
                data["Status"]
            )
        )
    if "FailureDescription" in data:
        import aws_sdk_firehose.types.failure_description

        out["failure_description"] = (
            aws_sdk_firehose.types.failure_description.deserialize_aws_json_1_1(
                data["FailureDescription"]
            )
        )
    return out
