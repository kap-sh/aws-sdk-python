"""Generated from Smithy shape ``com.amazonaws.kms#KeyLastUsageData``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.cloud_trail_event_id_type
    import awd_sdk_kms.types.date_type
    import awd_sdk_kms.types.key_last_usage_tracking_operation
    import awd_sdk_kms.types.kms_request_id_type


class KeyLastUsageData(TypedDict):
    operation: NotRequired[
        "awd_sdk_kms.types.key_last_usage_tracking_operation.KeyLastUsageTrackingOperation"
    ]
    """<p>The last successful cryptographic operation the KMS key was used for. Absent if the key has not been used since KMS began tracking.</p>"""
    timestamp: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>The date and time when the KMS key was most recently used for a successful cryptographic operation. Absent if the key has not been used since KMS began tracking.</p>"""
    cloud_trail_event_id: NotRequired[
        "awd_sdk_kms.types.cloud_trail_event_id_type.CloudTrailEventIdType"
    ]
    """<p>The CloudTrail <code>eventId</code> associated with the last successful cryptographic operation. Absent if the key has not been used since KMS began tracking.</p>"""
    kms_request_id: NotRequired[
        "awd_sdk_kms.types.kms_request_id_type.KmsRequestIdType"
    ]
    """<p>The KMS request ID associated with the last successful cryptographic operation. Absent if the key has not been used since KMS began tracking.</p>"""
