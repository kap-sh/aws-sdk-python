"""Generated from Smithy shape ``com.amazonaws.kms#GetKeyLastUsageResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.date_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.key_last_usage_data


class GetKeyLastUsageResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The globally unique identifier for the KMS key.</p>"""
    key_last_usage: NotRequired[
        "awd_sdk_kms.types.key_last_usage_data.KeyLastUsageData"
    ]
    """<p>Contains usage information about the last time the KMS key was used for a successful cryptographic operation. If the key has not been used since tracking began, this response element is empty.</p>"""
    tracking_start_date: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>The date from which KMS began recording cryptographic activity for this key, or the date the KMS key was created, whichever is later.</p>"""
    key_creation_date: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>The date and time when the KMS key was created.</p>"""
