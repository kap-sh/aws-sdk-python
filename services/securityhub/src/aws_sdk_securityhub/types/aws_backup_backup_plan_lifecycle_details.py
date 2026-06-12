"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsBackupBackupPlanLifecycleDetails``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.long


class AwsBackupBackupPlanLifecycleDetails(TypedDict):
    delete_after_days: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>Specifies the number of days after creation that a recovery point is deleted. Must be greater than 90 days plus <code>MoveToColdStorageAfterDays</code>. </p>"""
    move_to_cold_storage_after_days: NotRequired["aws_sdk_securityhub.types.long.Long"]
    """<p>Specifies the number of days after creation that a recovery point is moved to cold storage. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AwsBackupBackupPlanLifecycleDetails) -> dict:
    out: dict = {}
    if "delete_after_days" in value:
        out["DeleteAfterDays"] = value["delete_after_days"]
    if "move_to_cold_storage_after_days" in value:
        out["MoveToColdStorageAfterDays"] = value["move_to_cold_storage_after_days"]
    return out


def deserialize_json(data: dict) -> AwsBackupBackupPlanLifecycleDetails:
    out: AwsBackupBackupPlanLifecycleDetails = {}  # type: ignore[typeddict-item]
    if "DeleteAfterDays" in data:
        out["delete_after_days"] = data["DeleteAfterDays"]
    if "MoveToColdStorageAfterDays" in data:
        out["move_to_cold_storage_after_days"] = data["MoveToColdStorageAfterDays"]
    return out
