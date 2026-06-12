"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#PendingMaintenanceAction``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_database_migration_service.types.string
    import aws_sdk_database_migration_service.types.t_stamp


class PendingMaintenanceAction(TypedDict):
    action: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The type of pending maintenance action that is available for the resource.</p>"""
    auto_applied_after_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date of the maintenance window when the action is to be applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any <code>next-maintenance</code> opt-in requests are ignored.</p>"""
    forced_apply_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date when the maintenance action will be automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any <code>immediate</code> opt-in requests are ignored.</p>"""
    opt_in_status: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>The type of opt-in request that has been received for the resource.</p>"""
    current_apply_date: NotRequired[
        "aws_sdk_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The effective date when the pending maintenance action will be applied to the resource. This date takes into account opt-in requests received from the <code>ApplyPendingMaintenanceAction</code> API operation, and also the <code>AutoAppliedAfterDate</code> and <code>ForcedApplyDate</code> parameter values. This value is blank if an opt-in request has not been received and nothing has been specified for <code>AutoAppliedAfterDate</code> or <code>ForcedApplyDate</code>.</p>"""
    description: NotRequired["aws_sdk_database_migration_service.types.string.String"]
    """<p>A description providing more detail about the maintenance action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PendingMaintenanceAction) -> dict:
    out: dict = {}
    if "action" in value:
        out["Action"] = value["action"]
    if "auto_applied_after_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["AutoAppliedAfterDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["auto_applied_after_date"]
            )
        )
    if "forced_apply_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["ForcedApplyDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["forced_apply_date"]
            )
        )
    if "opt_in_status" in value:
        out["OptInStatus"] = value["opt_in_status"]
    if "current_apply_date" in value:
        import aws_sdk_database_migration_service.types.t_stamp

        out["CurrentApplyDate"] = (
            aws_sdk_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["current_apply_date"]
            )
        )
    if "description" in value:
        out["Description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> PendingMaintenanceAction:
    out: PendingMaintenanceAction = {}  # type: ignore[typeddict-item]
    if "Action" in data:
        out["action"] = data["Action"]
    if "AutoAppliedAfterDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["auto_applied_after_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["AutoAppliedAfterDate"]
            )
        )
    if "ForcedApplyDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["forced_apply_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ForcedApplyDate"]
            )
        )
    if "OptInStatus" in data:
        out["opt_in_status"] = data["OptInStatus"]
    if "CurrentApplyDate" in data:
        import aws_sdk_database_migration_service.types.t_stamp

        out["current_apply_date"] = (
            aws_sdk_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["CurrentApplyDate"]
            )
        )
    if "Description" in data:
        out["description"] = data["Description"]
    return out
