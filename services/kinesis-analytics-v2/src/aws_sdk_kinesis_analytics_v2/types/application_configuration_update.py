"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationConfigurationUpdate``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_code_configuration_update
    import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_update
    import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_update
    import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_update
    import aws_sdk_kinesis_analytics_v2.types.environment_property_updates
    import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_update
    import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_update
    import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_updates
    import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_update


class ApplicationConfigurationUpdate(TypedDict, closed=True):
    sql_application_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_update.SqlApplicationConfigurationUpdate"
    ]
    """<p>Describes updates to a SQL-based Kinesis Data Analytics application's configuration.</p>"""
    application_code_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_code_configuration_update.ApplicationCodeConfigurationUpdate"
    ]
    """<p>Describes updates to an application's code configuration.</p>"""
    flink_application_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_update.FlinkApplicationConfigurationUpdate"
    ]
    """<p>Describes updates to a Managed Service for Apache Flink application's configuration.</p>"""
    environment_property_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.environment_property_updates.EnvironmentPropertyUpdates"
    ]
    """<p>Describes updates to the environment properties for a Managed Service for Apache Flink application.</p>"""
    application_snapshot_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_update.ApplicationSnapshotConfigurationUpdate"
    ]
    """<p>Describes whether snapshots are enabled for a Managed Service for Apache Flink application.</p>"""
    application_system_rollback_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_update.ApplicationSystemRollbackConfigurationUpdate"
    ]
    """<p>Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.</p>"""
    vpc_configuration_updates: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.vpc_configuration_updates.VpcConfigurationUpdates"
    ]
    """<p>Updates to the array of descriptions of VPC configurations available to the application.</p>"""
    zeppelin_application_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_update.ZeppelinApplicationConfigurationUpdate"
    ]
    """<p>Updates to the configuration of a Managed Service for Apache Flink Studio notebook.</p>"""
    application_encryption_configuration_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_update.ApplicationEncryptionConfigurationUpdate"
    ]
    """<p>Represents an update for encryption at rest configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationConfigurationUpdate) -> dict:
    out: dict = {}
    if "sql_application_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_update

        out["SqlApplicationConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_update.serialize_aws_json_1_1(
                value["sql_application_configuration_update"]
            )
        )
    if "application_code_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_code_configuration_update

        out["ApplicationCodeConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.application_code_configuration_update.serialize_aws_json_1_1(
                value["application_code_configuration_update"]
            )
        )
    if "flink_application_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_update

        out["FlinkApplicationConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_update.serialize_aws_json_1_1(
                value["flink_application_configuration_update"]
            )
        )
    if "environment_property_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.environment_property_updates

        out["EnvironmentPropertyUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.environment_property_updates.serialize_aws_json_1_1(
                value["environment_property_updates"]
            )
        )
    if "application_snapshot_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_update

        out["ApplicationSnapshotConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_update.serialize_aws_json_1_1(
                value["application_snapshot_configuration_update"]
            )
        )
    if "application_system_rollback_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_update

        out["ApplicationSystemRollbackConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_update.serialize_aws_json_1_1(
                value["application_system_rollback_configuration_update"]
            )
        )
    if "vpc_configuration_updates" in value:
        import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_updates

        out["VpcConfigurationUpdates"] = (
            aws_sdk_kinesis_analytics_v2.types.vpc_configuration_updates.serialize_aws_json_1_1(
                value["vpc_configuration_updates"]
            )
        )
    if "zeppelin_application_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_update

        out["ZeppelinApplicationConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_update.serialize_aws_json_1_1(
                value["zeppelin_application_configuration_update"]
            )
        )
    if "application_encryption_configuration_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_update

        out["ApplicationEncryptionConfigurationUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_update.serialize_aws_json_1_1(
                value["application_encryption_configuration_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationConfigurationUpdate:
    out: ApplicationConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "SqlApplicationConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_update

        out["sql_application_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_update.deserialize_aws_json_1_1(
                data["SqlApplicationConfigurationUpdate"]
            )
        )
    if "ApplicationCodeConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_code_configuration_update

        out["application_code_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.application_code_configuration_update.deserialize_aws_json_1_1(
                data["ApplicationCodeConfigurationUpdate"]
            )
        )
    if "FlinkApplicationConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_update

        out["flink_application_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_update.deserialize_aws_json_1_1(
                data["FlinkApplicationConfigurationUpdate"]
            )
        )
    if "EnvironmentPropertyUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.environment_property_updates

        out["environment_property_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.environment_property_updates.deserialize_aws_json_1_1(
                data["EnvironmentPropertyUpdates"]
            )
        )
    if "ApplicationSnapshotConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_update

        out["application_snapshot_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_update.deserialize_aws_json_1_1(
                data["ApplicationSnapshotConfigurationUpdate"]
            )
        )
    if "ApplicationSystemRollbackConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_update

        out["application_system_rollback_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_update.deserialize_aws_json_1_1(
                data["ApplicationSystemRollbackConfigurationUpdate"]
            )
        )
    if "VpcConfigurationUpdates" in data:
        import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_updates

        out["vpc_configuration_updates"] = (
            aws_sdk_kinesis_analytics_v2.types.vpc_configuration_updates.deserialize_aws_json_1_1(
                data["VpcConfigurationUpdates"]
            )
        )
    if "ZeppelinApplicationConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_update

        out["zeppelin_application_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_update.deserialize_aws_json_1_1(
                data["ZeppelinApplicationConfigurationUpdate"]
            )
        )
    if "ApplicationEncryptionConfigurationUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_update

        out["application_encryption_configuration_update"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_update.deserialize_aws_json_1_1(
                data["ApplicationEncryptionConfigurationUpdate"]
            )
        )
    return out
