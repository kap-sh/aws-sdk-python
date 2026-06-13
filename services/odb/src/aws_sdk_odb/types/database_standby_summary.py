"""Generated from Smithy shape ``com.amazonaws.odb#DatabaseStandbySummary``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import datetime

    import aws_sdk_odb.types.autonomous_database_resource_status


class DatabaseStandbySummary(TypedDict):
    availability_domain: NotRequired["str"]
    """<p>The availability domain of the standby Autonomous Database.</p>"""
    lag_time_in_seconds: NotRequired["int"]
    """<p>The time lag, in seconds, between the standby database and the primary database.</p>"""
    status: NotRequired[
        "aws_sdk_odb.types.autonomous_database_resource_status.AutonomousDatabaseResourceStatus"
    ]
    """<p>The current status of the standby Autonomous Database.</p>"""
    status_reason: NotRequired["str"]
    """<p>Additional information about the current status of the standby Autonomous Database, if applicable.</p>"""
    maintenance_target_component: NotRequired["str"]
    """<p>The component on the standby Autonomous Database that the current maintenance is being applied to.</p>"""
    time_data_guard_role_changed: NotRequired["datetime.datetime"]
    """<p>The date and time when the Oracle Data Guard role of the standby database last changed.</p>"""
    time_disaster_recovery_role_changed: NotRequired["datetime.datetime"]
    """<p>The date and time when the disaster recovery role of the standby database last changed.</p>"""
    time_maintenance_begin: NotRequired["datetime.datetime"]
    """<p>The date and time when the next maintenance of the standby database begins.</p>"""
    time_maintenance_end: NotRequired["datetime.datetime"]
    """<p>The date and time when the next maintenance of the standby database ends.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DatabaseStandbySummary) -> dict:
    out: dict = {}
    if "availability_domain" in value:
        out["availabilityDomain"] = value["availability_domain"]
    if "lag_time_in_seconds" in value:
        out["lagTimeInSeconds"] = value["lag_time_in_seconds"]
    if "status" in value:
        import aws_sdk_odb.types.autonomous_database_resource_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_resource_status.serialize_aws_json_1_0(
                value["status"]
            )
        )
    if "status_reason" in value:
        out["statusReason"] = value["status_reason"]
    if "maintenance_target_component" in value:
        out["maintenanceTargetComponent"] = value["maintenance_target_component"]
    if "time_data_guard_role_changed" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeDataGuardRoleChanged"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_data_guard_role_changed"]
            )
        )
    if "time_disaster_recovery_role_changed" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeDisasterRecoveryRoleChanged"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_disaster_recovery_role_changed"]
            )
        )
    if "time_maintenance_begin" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeMaintenanceBegin"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_maintenance_begin"]
            )
        )
    if "time_maintenance_end" in value:
        import aws_sdk_odb.types._prelude.timestamp

        out["timeMaintenanceEnd"] = (
            aws_sdk_odb.types._prelude.timestamp.serialize_aws_json_1_0(
                value["time_maintenance_end"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> DatabaseStandbySummary:
    out: DatabaseStandbySummary = {}  # type: ignore[typeddict-item]
    if "availabilityDomain" in data:
        out["availability_domain"] = data["availabilityDomain"]
    if "lagTimeInSeconds" in data:
        out["lag_time_in_seconds"] = data["lagTimeInSeconds"]
    if "status" in data:
        import aws_sdk_odb.types.autonomous_database_resource_status

        out["status"] = (
            aws_sdk_odb.types.autonomous_database_resource_status.deserialize_aws_json_1_0(
                data["status"]
            )
        )
    if "statusReason" in data:
        out["status_reason"] = data["statusReason"]
    if "maintenanceTargetComponent" in data:
        out["maintenance_target_component"] = data["maintenanceTargetComponent"]
    if "timeDataGuardRoleChanged" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_data_guard_role_changed"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeDataGuardRoleChanged"]
            )
        )
    if "timeDisasterRecoveryRoleChanged" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_disaster_recovery_role_changed"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeDisasterRecoveryRoleChanged"]
            )
        )
    if "timeMaintenanceBegin" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_maintenance_begin"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeMaintenanceBegin"]
            )
        )
    if "timeMaintenanceEnd" in data:
        import aws_sdk_odb.types._prelude.timestamp

        out["time_maintenance_end"] = (
            aws_sdk_odb.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["timeMaintenanceEnd"]
            )
        )
    return out
