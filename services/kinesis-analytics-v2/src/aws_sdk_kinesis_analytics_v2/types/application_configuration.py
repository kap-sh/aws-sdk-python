"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_code_configuration
    import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration
    import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration
    import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration
    import aws_sdk_kinesis_analytics_v2.types.environment_properties
    import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration
    import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration
    import aws_sdk_kinesis_analytics_v2.types.vpc_configurations
    import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration


class ApplicationConfiguration(TypedDict):
    sql_application_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.sql_application_configuration.SqlApplicationConfiguration"
    ]
    """<p>The creation and update parameters for a SQL-based Kinesis Data Analytics application.</p>"""
    flink_application_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.flink_application_configuration.FlinkApplicationConfiguration"
    ]
    """<p>The creation and update parameters for a Managed Service for Apache Flink application.</p>"""
    environment_properties: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.environment_properties.EnvironmentProperties"
    ]
    """<p>Describes execution properties for a Managed Service for Apache Flink application.</p>"""
    application_code_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_code_configuration.ApplicationCodeConfiguration"
    ]
    """<p>The code location and type parameters for a Managed Service for Apache Flink application.</p>"""
    application_snapshot_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration.ApplicationSnapshotConfiguration"
    ]
    """<p>Describes whether snapshots are enabled for a Managed Service for Apache Flink application.</p>"""
    application_system_rollback_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration.ApplicationSystemRollbackConfiguration"
    ]
    """<p>Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.</p>"""
    vpc_configurations: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.vpc_configurations.VpcConfigurations"
    ]
    """<p>The array of descriptions of VPC configurations available to the application.</p>"""
    zeppelin_application_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration.ZeppelinApplicationConfiguration"
    ]
    """<p>The configuration parameters for a Managed Service for Apache Flink Studio notebook.</p>"""
    application_encryption_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration.ApplicationEncryptionConfiguration"
    ]
    """<p>The configuration to manage encryption at rest.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationConfiguration) -> dict:
    out: dict = {}
    if "sql_application_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration

        out["SqlApplicationConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.sql_application_configuration.serialize_aws_json_1_1(
                value["sql_application_configuration"]
            )
        )
    if "flink_application_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration

        out["FlinkApplicationConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_application_configuration.serialize_aws_json_1_1(
                value["flink_application_configuration"]
            )
        )
    if "environment_properties" in value:
        import aws_sdk_kinesis_analytics_v2.types.environment_properties

        out["EnvironmentProperties"] = (
            aws_sdk_kinesis_analytics_v2.types.environment_properties.serialize_aws_json_1_1(
                value["environment_properties"]
            )
        )
    if "application_code_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_code_configuration

        out["ApplicationCodeConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_code_configuration.serialize_aws_json_1_1(
                value["application_code_configuration"]
            )
        )
    if "application_snapshot_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration

        out["ApplicationSnapshotConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration.serialize_aws_json_1_1(
                value["application_snapshot_configuration"]
            )
        )
    if "application_system_rollback_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration

        out["ApplicationSystemRollbackConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration.serialize_aws_json_1_1(
                value["application_system_rollback_configuration"]
            )
        )
    if "vpc_configurations" in value:
        import aws_sdk_kinesis_analytics_v2.types.vpc_configurations

        out["VpcConfigurations"] = (
            aws_sdk_kinesis_analytics_v2.types.vpc_configurations.serialize_aws_json_1_1(
                value["vpc_configurations"]
            )
        )
    if "zeppelin_application_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration

        out["ZeppelinApplicationConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration.serialize_aws_json_1_1(
                value["zeppelin_application_configuration"]
            )
        )
    if "application_encryption_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration

        out["ApplicationEncryptionConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration.serialize_aws_json_1_1(
                value["application_encryption_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationConfiguration:
    out: ApplicationConfiguration = {}  # type: ignore[typeddict-item]
    if "SqlApplicationConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration

        out["sql_application_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.sql_application_configuration.deserialize_aws_json_1_1(
                data["SqlApplicationConfiguration"]
            )
        )
    if "FlinkApplicationConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration

        out["flink_application_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_application_configuration.deserialize_aws_json_1_1(
                data["FlinkApplicationConfiguration"]
            )
        )
    if "EnvironmentProperties" in data:
        import aws_sdk_kinesis_analytics_v2.types.environment_properties

        out["environment_properties"] = (
            aws_sdk_kinesis_analytics_v2.types.environment_properties.deserialize_aws_json_1_1(
                data["EnvironmentProperties"]
            )
        )
    if "ApplicationCodeConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_code_configuration

        out["application_code_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_code_configuration.deserialize_aws_json_1_1(
                data["ApplicationCodeConfiguration"]
            )
        )
    if "ApplicationSnapshotConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration

        out["application_snapshot_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration.deserialize_aws_json_1_1(
                data["ApplicationSnapshotConfiguration"]
            )
        )
    if "ApplicationSystemRollbackConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration

        out["application_system_rollback_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration.deserialize_aws_json_1_1(
                data["ApplicationSystemRollbackConfiguration"]
            )
        )
    if "VpcConfigurations" in data:
        import aws_sdk_kinesis_analytics_v2.types.vpc_configurations

        out["vpc_configurations"] = (
            aws_sdk_kinesis_analytics_v2.types.vpc_configurations.deserialize_aws_json_1_1(
                data["VpcConfigurations"]
            )
        )
    if "ZeppelinApplicationConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration

        out["zeppelin_application_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration.deserialize_aws_json_1_1(
                data["ZeppelinApplicationConfiguration"]
            )
        )
    if "ApplicationEncryptionConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration

        out["application_encryption_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration.deserialize_aws_json_1_1(
                data["ApplicationEncryptionConfiguration"]
            )
        )
    return out
