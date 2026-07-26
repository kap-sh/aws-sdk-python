"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#ApplyPendingMaintenanceActionMessage``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_database_migration_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_database_migration_service.types.string


class ApplyPendingMaintenanceActionMessage(TypedDict, closed=True):
    replication_instance_arn: "capo_database_migration_service.types.string.String"
    """<p>The Amazon Resource Name (ARN) of the DMS resource that the pending maintenance action applies to.</p>"""
    apply_action: "capo_database_migration_service.types.string.String"
    """<p>The pending maintenance action to apply to this resource.</p> <p>Valid values: <code>os-upgrade</code>, <code>system-update</code>, <code>db-upgrade</code>, <code>os-patch</code> </p>"""
    opt_in_type: "capo_database_migration_service.types.string.String"
    """<p>A value that specifies the type of opt-in request, or undoes an opt-in request. You can't undo an opt-in request of type <code>immediate</code>.</p> <p>Valid values:</p> <ul> <li> <p> <code>immediate</code> - Apply the maintenance action immediately.</p> </li> <li> <p> <code>next-maintenance</code> - Apply the maintenance action during the next maintenance window for the resource.</p> </li> <li> <p> <code>undo-opt-in</code> - Cancel any existing <code>next-maintenance</code> opt-in requests.</p> </li> </ul>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplyPendingMaintenanceActionMessage) -> dict:
    out: dict = {}
    out["ReplicationInstanceArn"] = value["replication_instance_arn"]
    out["ApplyAction"] = value["apply_action"]
    out["OptInType"] = value["opt_in_type"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplyPendingMaintenanceActionMessage:
    out: ApplyPendingMaintenanceActionMessage = {}  # type: ignore[typeddict-item]
    if "ReplicationInstanceArn" in data:
        out["replication_instance_arn"] = data["ReplicationInstanceArn"]
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionMessage.replication_instance_arn required"
        )
    if "ApplyAction" in data:
        out["apply_action"] = data["ApplyAction"]
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionMessage.apply_action required"
        )
    if "OptInType" in data:
        out["opt_in_type"] = data["OptInType"]
    else:
        raise DeserializationError(
            "ApplyPendingMaintenanceActionMessage.opt_in_type required"
        )
    return out
