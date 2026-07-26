"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsSqsQueueDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.integer
    import capo_securityhub.types.non_empty_string


class AwsSqsQueueDetails(TypedDict, closed=True):
    kms_data_key_reuse_period_seconds: NotRequired[
        "capo_securityhub.types.integer.Integer"
    ]
    """<p>The length of time, in seconds, for which Amazon SQS can reuse a data key to encrypt or decrypt messages before calling KMS again.</p>"""
    kms_master_key_id: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ID of an Amazon Web Services managed key for Amazon SQS or a custom KMS key.</p>"""
    queue_name: NotRequired["capo_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>The name of the new queue.</p>"""
    dead_letter_target_arn: NotRequired[
        "capo_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>The ARN of the dead-letter queue to which Amazon SQS moves messages after the value of <code>maxReceiveCount</code> is exceeded. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsSqsQueueDetails) -> dict:
    out: dict = {}
    if "kms_data_key_reuse_period_seconds" in value:
        out["KmsDataKeyReusePeriodSeconds"] = value["kms_data_key_reuse_period_seconds"]
    if "kms_master_key_id" in value:
        out["KmsMasterKeyId"] = value["kms_master_key_id"]
    if "queue_name" in value:
        out["QueueName"] = value["queue_name"]
    if "dead_letter_target_arn" in value:
        out["DeadLetterTargetArn"] = value["dead_letter_target_arn"]
    return out


def deserialize_json(data: dict) -> AwsSqsQueueDetails:
    out: AwsSqsQueueDetails = {}  # type: ignore[typeddict-item]
    if "KmsDataKeyReusePeriodSeconds" in data:
        out["kms_data_key_reuse_period_seconds"] = data["KmsDataKeyReusePeriodSeconds"]
    if "KmsMasterKeyId" in data:
        out["kms_master_key_id"] = data["KmsMasterKeyId"]
    if "QueueName" in data:
        out["queue_name"] = data["QueueName"]
    if "DeadLetterTargetArn" in data:
        out["dead_letter_target_arn"] = data["DeadLetterTargetArn"]
    return out
