"""Generated from Smithy shape ``com.amazonaws.kms#KeyLastUsageData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kms.types.cloud_trail_event_id_type
    import aws_sdk_kms.types.date_type
    import aws_sdk_kms.types.key_last_usage_tracking_operation
    import aws_sdk_kms.types.kms_request_id_type


class KeyLastUsageData(TypedDict):
    operation: NotRequired[
        "aws_sdk_kms.types.key_last_usage_tracking_operation.KeyLastUsageTrackingOperation"
    ]
    """<p>The last successful cryptographic operation the KMS key was used for. Absent if the key has not been used since KMS began tracking.</p>"""
    timestamp: NotRequired["aws_sdk_kms.types.date_type.DateType"]
    """<p>The date and time when the KMS key was most recently used for a successful cryptographic operation. Absent if the key has not been used since KMS began tracking.</p>"""
    cloud_trail_event_id: NotRequired[
        "aws_sdk_kms.types.cloud_trail_event_id_type.CloudTrailEventIdType"
    ]
    """<p>The CloudTrail <code>eventId</code> associated with the last successful cryptographic operation. Absent if the key has not been used since KMS began tracking.</p>"""
    kms_request_id: NotRequired[
        "aws_sdk_kms.types.kms_request_id_type.KmsRequestIdType"
    ]
    """<p>The KMS request ID associated with the last successful cryptographic operation. Absent if the key has not been used since KMS began tracking.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyLastUsageData) -> dict:
    out: dict = {}
    if "operation" in value:
        import aws_sdk_kms.types.key_last_usage_tracking_operation

        out["Operation"] = (
            aws_sdk_kms.types.key_last_usage_tracking_operation.serialize_aws_json_1_1(
                value["operation"]
            )
        )
    if "timestamp" in value:
        import aws_sdk_kms.types.date_type

        out["Timestamp"] = aws_sdk_kms.types.date_type.serialize_aws_json_1_1(
            value["timestamp"]
        )
    if "cloud_trail_event_id" in value:
        out["CloudTrailEventId"] = value["cloud_trail_event_id"]
    if "kms_request_id" in value:
        out["KmsRequestId"] = value["kms_request_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> KeyLastUsageData:
    out: KeyLastUsageData = {}  # type: ignore[typeddict-item]
    if "Operation" in data:
        import aws_sdk_kms.types.key_last_usage_tracking_operation

        out["operation"] = (
            aws_sdk_kms.types.key_last_usage_tracking_operation.deserialize_aws_json_1_1(
                data["Operation"]
            )
        )
    if "Timestamp" in data:
        import aws_sdk_kms.types.date_type

        out["timestamp"] = aws_sdk_kms.types.date_type.deserialize_aws_json_1_1(
            data["Timestamp"]
        )
    if "CloudTrailEventId" in data:
        out["cloud_trail_event_id"] = data["CloudTrailEventId"]
    if "KmsRequestId" in data:
        out["kms_request_id"] = data["KmsRequestId"]
    return out
