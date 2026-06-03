"""Generated from Smithy shape ``com.amazonaws.kms#ScheduleKeyDeletionResponse``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import awd_sdk_kms.types.date_type
    import awd_sdk_kms.types.key_id_type
    import awd_sdk_kms.types.key_state
    import awd_sdk_kms.types.pending_window_in_days_type


class ScheduleKeyDeletionResponse(TypedDict):
    key_id: NotRequired["awd_sdk_kms.types.key_id_type.KeyIdType"]
    """<p>The Amazon Resource Name (<a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN\">key ARN</a>) of the KMS key whose deletion is scheduled.</p>"""
    deletion_date: NotRequired["awd_sdk_kms.types.date_type.DateType"]
    """<p>The date and time after which KMS deletes the KMS key.</p> <p>If the KMS key is a multi-Region primary key with replica keys, this field does not appear. The deletion date for the primary key isn't known until its last replica key is deleted.</p>"""
    key_state: NotRequired["awd_sdk_kms.types.key_state.KeyState"]
    """<p>The current status of the KMS key.</p> <p>For more information about how key state affects the use of a KMS key, see <a href=\"https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html\">Key states of KMS keys</a> in the <i>Key Management Service Developer Guide</i>.</p>"""
    pending_window_in_days: NotRequired[
        "awd_sdk_kms.types.pending_window_in_days_type.PendingWindowInDaysType"
    ]
    """<p>The waiting period before the KMS key is deleted. </p> <p>If the KMS key is a multi-Region primary key with replicas, the waiting period begins when the last of its replica keys is deleted. Otherwise, the waiting period begins immediately.</p>"""
