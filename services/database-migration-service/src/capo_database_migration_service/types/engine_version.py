"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#EngineVersion``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_database_migration_service.types.available_upgrades_list
    import capo_database_migration_service.types.release_status_values
    import capo_database_migration_service.types.string
    import capo_database_migration_service.types.t_stamp


class EngineVersion(TypedDict, closed=True):
    version: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The version number of the replication instance.</p>"""
    lifecycle: NotRequired["capo_database_migration_service.types.string.String"]
    """<p>The lifecycle status of the replication instance version. Valid values are <code>DEPRECATED</code>, <code>DEFAULT_VERSION</code>, and <code>ACTIVE</code>.</p>"""
    release_status: NotRequired[
        "capo_database_migration_service.types.release_status_values.ReleaseStatusValues"
    ]
    """<p>The release status of the replication instance version.</p>"""
    launch_date: NotRequired["capo_database_migration_service.types.t_stamp.TStamp"]
    """<p>The date when the replication instance version became publicly available.</p>"""
    auto_upgrade_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date when the replication instance will be automatically upgraded. This setting only applies if the <code>auto-minor-version</code> setting is enabled.</p>"""
    deprecation_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date when the replication instance version will be deprecated and can no longer be requested.</p>"""
    force_upgrade_date: NotRequired[
        "capo_database_migration_service.types.t_stamp.TStamp"
    ]
    """<p>The date when the replication instance will have a version upgrade forced.</p>"""
    available_upgrades: NotRequired[
        "capo_database_migration_service.types.available_upgrades_list.AvailableUpgradesList"
    ]
    """<p>The list of valid replication instance versions that you can upgrade to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EngineVersion) -> dict:
    out: dict = {}
    if "version" in value:
        out["Version"] = value["version"]
    if "lifecycle" in value:
        out["Lifecycle"] = value["lifecycle"]
    if "release_status" in value:
        import capo_database_migration_service.types.release_status_values

        out["ReleaseStatus"] = (
            capo_database_migration_service.types.release_status_values.serialize_aws_json_1_1(
                value["release_status"]
            )
        )
    if "launch_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["LaunchDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["launch_date"]
            )
        )
    if "auto_upgrade_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["AutoUpgradeDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["auto_upgrade_date"]
            )
        )
    if "deprecation_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["DeprecationDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["deprecation_date"]
            )
        )
    if "force_upgrade_date" in value:
        import capo_database_migration_service.types.t_stamp

        out["ForceUpgradeDate"] = (
            capo_database_migration_service.types.t_stamp.serialize_aws_json_1_1(
                value["force_upgrade_date"]
            )
        )
    if "available_upgrades" in value:
        import capo_database_migration_service.types.available_upgrades_list

        out["AvailableUpgrades"] = (
            capo_database_migration_service.types.available_upgrades_list.serialize_aws_json_1_1(
                value["available_upgrades"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> EngineVersion:
    out: EngineVersion = {}  # type: ignore[typeddict-item]
    if "Version" in data:
        out["version"] = data["Version"]
    if "Lifecycle" in data:
        out["lifecycle"] = data["Lifecycle"]
    if "ReleaseStatus" in data:
        import capo_database_migration_service.types.release_status_values

        out["release_status"] = (
            capo_database_migration_service.types.release_status_values.deserialize_aws_json_1_1(
                data["ReleaseStatus"]
            )
        )
    if "LaunchDate" in data:
        import capo_database_migration_service.types.t_stamp

        out["launch_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["LaunchDate"]
            )
        )
    if "AutoUpgradeDate" in data:
        import capo_database_migration_service.types.t_stamp

        out["auto_upgrade_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["AutoUpgradeDate"]
            )
        )
    if "DeprecationDate" in data:
        import capo_database_migration_service.types.t_stamp

        out["deprecation_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["DeprecationDate"]
            )
        )
    if "ForceUpgradeDate" in data:
        import capo_database_migration_service.types.t_stamp

        out["force_upgrade_date"] = (
            capo_database_migration_service.types.t_stamp.deserialize_aws_json_1_1(
                data["ForceUpgradeDate"]
            )
        )
    if "AvailableUpgrades" in data:
        import capo_database_migration_service.types.available_upgrades_list

        out["available_upgrades"] = (
            capo_database_migration_service.types.available_upgrades_list.deserialize_aws_json_1_1(
                data["AvailableUpgrades"]
            )
        )
    return out
