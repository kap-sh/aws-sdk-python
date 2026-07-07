"""Generated from Smithy shape ``com.amazonaws.odb#SourceConfiguration``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from aws_sdk_odb.errors import DeserializationError, SerializationError

if TYPE_CHECKING:
    import aws_sdk_odb.types.clone_to_refreshable_configuration
    import aws_sdk_odb.types.cross_region_data_guard_configuration
    import aws_sdk_odb.types.cross_region_disaster_recovery_configuration
    import aws_sdk_odb.types.database_clone_configuration
    import aws_sdk_odb.types.point_in_time_restore_configuration
    import aws_sdk_odb.types.restore_from_backup_configuration


class _SourceConfiguration_databaseClone(TypedDict, closed=True):
    databaseClone: (
        "aws_sdk_odb.types.database_clone_configuration.DatabaseCloneConfiguration"
    )


class _SourceConfiguration_restoreFromBackup(TypedDict, closed=True):
    restoreFromBackup: "aws_sdk_odb.types.restore_from_backup_configuration.RestoreFromBackupConfiguration"


class _SourceConfiguration_pointInTimeRestore(TypedDict, closed=True):
    pointInTimeRestore: "aws_sdk_odb.types.point_in_time_restore_configuration.PointInTimeRestoreConfiguration"


class _SourceConfiguration_crossRegionDataGuard(TypedDict, closed=True):
    crossRegionDataGuard: "aws_sdk_odb.types.cross_region_data_guard_configuration.CrossRegionDataGuardConfiguration"


class _SourceConfiguration_crossRegionDisasterRecovery(TypedDict, closed=True):
    crossRegionDisasterRecovery: "aws_sdk_odb.types.cross_region_disaster_recovery_configuration.CrossRegionDisasterRecoveryConfiguration"


class _SourceConfiguration_cloneToRefreshable(TypedDict, closed=True):
    cloneToRefreshable: "aws_sdk_odb.types.clone_to_refreshable_configuration.CloneToRefreshableConfiguration"


SourceConfiguration: TypeAlias = (
    _SourceConfiguration_databaseClone
    | _SourceConfiguration_restoreFromBackup
    | _SourceConfiguration_pointInTimeRestore
    | _SourceConfiguration_crossRegionDataGuard
    | _SourceConfiguration_crossRegionDisasterRecovery
    | _SourceConfiguration_cloneToRefreshable
)


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SourceConfiguration) -> dict:
    if "databaseClone" in value:
        import aws_sdk_odb.types.database_clone_configuration

        return {
            "databaseClone": aws_sdk_odb.types.database_clone_configuration.serialize_aws_json_1_0(
                value["databaseClone"]
            )
        }
    elif "restoreFromBackup" in value:
        import aws_sdk_odb.types.restore_from_backup_configuration

        return {
            "restoreFromBackup": aws_sdk_odb.types.restore_from_backup_configuration.serialize_aws_json_1_0(
                value["restoreFromBackup"]
            )
        }
    elif "pointInTimeRestore" in value:
        import aws_sdk_odb.types.point_in_time_restore_configuration

        return {
            "pointInTimeRestore": aws_sdk_odb.types.point_in_time_restore_configuration.serialize_aws_json_1_0(
                value["pointInTimeRestore"]
            )
        }
    elif "crossRegionDataGuard" in value:
        import aws_sdk_odb.types.cross_region_data_guard_configuration

        return {
            "crossRegionDataGuard": aws_sdk_odb.types.cross_region_data_guard_configuration.serialize_aws_json_1_0(
                value["crossRegionDataGuard"]
            )
        }
    elif "crossRegionDisasterRecovery" in value:
        import aws_sdk_odb.types.cross_region_disaster_recovery_configuration

        return {
            "crossRegionDisasterRecovery": aws_sdk_odb.types.cross_region_disaster_recovery_configuration.serialize_aws_json_1_0(
                value["crossRegionDisasterRecovery"]
            )
        }
    elif "cloneToRefreshable" in value:
        import aws_sdk_odb.types.clone_to_refreshable_configuration

        return {
            "cloneToRefreshable": aws_sdk_odb.types.clone_to_refreshable_configuration.serialize_aws_json_1_0(
                value["cloneToRefreshable"]
            )
        }
    else:
        raise SerializationError("SourceConfiguration: no variant present")


def deserialize_aws_json_1_0(data: dict) -> SourceConfiguration:
    if "databaseClone" in data:
        import aws_sdk_odb.types.database_clone_configuration

        return {
            "databaseClone": aws_sdk_odb.types.database_clone_configuration.deserialize_aws_json_1_0(
                data["databaseClone"]
            )
        }
    elif "restoreFromBackup" in data:
        import aws_sdk_odb.types.restore_from_backup_configuration

        return {
            "restoreFromBackup": aws_sdk_odb.types.restore_from_backup_configuration.deserialize_aws_json_1_0(
                data["restoreFromBackup"]
            )
        }
    elif "pointInTimeRestore" in data:
        import aws_sdk_odb.types.point_in_time_restore_configuration

        return {
            "pointInTimeRestore": aws_sdk_odb.types.point_in_time_restore_configuration.deserialize_aws_json_1_0(
                data["pointInTimeRestore"]
            )
        }
    elif "crossRegionDataGuard" in data:
        import aws_sdk_odb.types.cross_region_data_guard_configuration

        return {
            "crossRegionDataGuard": aws_sdk_odb.types.cross_region_data_guard_configuration.deserialize_aws_json_1_0(
                data["crossRegionDataGuard"]
            )
        }
    elif "crossRegionDisasterRecovery" in data:
        import aws_sdk_odb.types.cross_region_disaster_recovery_configuration

        return {
            "crossRegionDisasterRecovery": aws_sdk_odb.types.cross_region_disaster_recovery_configuration.deserialize_aws_json_1_0(
                data["crossRegionDisasterRecovery"]
            )
        }
    elif "cloneToRefreshable" in data:
        import aws_sdk_odb.types.clone_to_refreshable_configuration

        return {
            "cloneToRefreshable": aws_sdk_odb.types.clone_to_refreshable_configuration.deserialize_aws_json_1_0(
                data["cloneToRefreshable"]
            )
        }
    else:
        raise DeserializationError("SourceConfiguration: no recognized variant key")
