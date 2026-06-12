"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupRecoveryPointCalculatedLifecycleDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.non_empty_string


class AwsBackupRecoveryPointCalculatedLifecycleDetails(TypedDict):
    delete_at: NotRequired["aws_sdk_securityhub.types.non_empty_string.NonEmptyString"]
    """<p>Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus <code>MoveToColdStorageAfterDays</code>. </p>"""
    move_to_cold_storage_at: NotRequired[
        "aws_sdk_securityhub.types.non_empty_string.NonEmptyString"
    ]
    """<p>Specifies the number of days after creation that a recovery point is moved to cold storage. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupRecoveryPointCalculatedLifecycleDetails) -> dict:
    out: dict = {}
    if "delete_at" in value:
        out["DeleteAt"] = value["delete_at"]
    if "move_to_cold_storage_at" in value:
        out["MoveToColdStorageAt"] = value["move_to_cold_storage_at"]
    return out


def deserialize_json(data: dict) -> AwsBackupRecoveryPointCalculatedLifecycleDetails:
    out: AwsBackupRecoveryPointCalculatedLifecycleDetails = {}  # type: ignore[typeddict-item]
    if "DeleteAt" in data:
        out["delete_at"] = data["DeleteAt"]
    if "MoveToColdStorageAt" in data:
        out["move_to_cold_storage_at"] = data["MoveToColdStorageAt"]
    return out
