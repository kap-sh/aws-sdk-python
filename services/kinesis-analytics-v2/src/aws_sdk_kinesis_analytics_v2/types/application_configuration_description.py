"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ApplicationConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_code_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.environment_property_descriptions
    import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.run_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_description
    import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_descriptions
    import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_description


class ApplicationConfigurationDescription(TypedDict, closed=True):
    sql_application_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_description.SqlApplicationConfigurationDescription"
    ]
    """<p>The details about inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.</p>"""
    application_code_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_code_configuration_description.ApplicationCodeConfigurationDescription"
    ]
    """<p>The details about the application code for a Managed Service for Apache Flink application.</p>"""
    run_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.run_configuration_description.RunConfigurationDescription"
    ]
    """<p>The details about the starting properties for a Managed Service for Apache Flink application.</p>"""
    flink_application_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_description.FlinkApplicationConfigurationDescription"
    ]
    """<p>The details about a Managed Service for Apache Flink application.</p>"""
    environment_property_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.environment_property_descriptions.EnvironmentPropertyDescriptions"
    ]
    """<p>Describes execution properties for a Managed Service for Apache Flink application.</p>"""
    application_snapshot_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_description.ApplicationSnapshotConfigurationDescription"
    ]
    """<p>Describes whether snapshots are enabled for a Managed Service for Apache Flink application.</p>"""
    application_system_rollback_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_description.ApplicationSystemRollbackConfigurationDescription"
    ]
    """<p>Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application.</p>"""
    vpc_configuration_descriptions: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.vpc_configuration_descriptions.VpcConfigurationDescriptions"
    ]
    """<p>The array of descriptions of VPC configurations available to the application.</p>"""
    zeppelin_application_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_description.ZeppelinApplicationConfigurationDescription"
    ]
    """<p>The configuration parameters for a Managed Service for Apache Flink Studio notebook.</p>"""
    application_encryption_configuration_description: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description.ApplicationEncryptionConfigurationDescription"
    ]
    """<p>Describes the encryption at rest configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ApplicationConfigurationDescription) -> dict:
    out: dict = {}
    if "sql_application_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_description

        out["SqlApplicationConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_description.serialize_aws_json_1_1(
                value["sql_application_configuration_description"]
            )
        )
    if "application_code_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_code_configuration_description

        out["ApplicationCodeConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_code_configuration_description.serialize_aws_json_1_1(
                value["application_code_configuration_description"]
            )
        )
    if "run_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.run_configuration_description

        out["RunConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.run_configuration_description.serialize_aws_json_1_1(
                value["run_configuration_description"]
            )
        )
    if "flink_application_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_description

        out["FlinkApplicationConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_description.serialize_aws_json_1_1(
                value["flink_application_configuration_description"]
            )
        )
    if "environment_property_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.environment_property_descriptions

        out["EnvironmentPropertyDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.environment_property_descriptions.serialize_aws_json_1_1(
                value["environment_property_descriptions"]
            )
        )
    if "application_snapshot_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_description

        out["ApplicationSnapshotConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_description.serialize_aws_json_1_1(
                value["application_snapshot_configuration_description"]
            )
        )
    if "application_system_rollback_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_description

        out["ApplicationSystemRollbackConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_description.serialize_aws_json_1_1(
                value["application_system_rollback_configuration_description"]
            )
        )
    if "vpc_configuration_descriptions" in value:
        import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_descriptions

        out["VpcConfigurationDescriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.vpc_configuration_descriptions.serialize_aws_json_1_1(
                value["vpc_configuration_descriptions"]
            )
        )
    if "zeppelin_application_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_description

        out["ZeppelinApplicationConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_description.serialize_aws_json_1_1(
                value["zeppelin_application_configuration_description"]
            )
        )
    if "application_encryption_configuration_description" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description

        out["ApplicationEncryptionConfigurationDescription"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description.serialize_aws_json_1_1(
                value["application_encryption_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ApplicationConfigurationDescription:
    out: ApplicationConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "SqlApplicationConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_description

        out["sql_application_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.sql_application_configuration_description.deserialize_aws_json_1_1(
                data["SqlApplicationConfigurationDescription"]
            )
        )
    if "ApplicationCodeConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_code_configuration_description

        out["application_code_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_code_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationCodeConfigurationDescription"]
            )
        )
    if "RunConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.run_configuration_description

        out["run_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.run_configuration_description.deserialize_aws_json_1_1(
                data["RunConfigurationDescription"]
            )
        )
    if "FlinkApplicationConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_description

        out["flink_application_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_application_configuration_description.deserialize_aws_json_1_1(
                data["FlinkApplicationConfigurationDescription"]
            )
        )
    if "EnvironmentPropertyDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.environment_property_descriptions

        out["environment_property_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.environment_property_descriptions.deserialize_aws_json_1_1(
                data["EnvironmentPropertyDescriptions"]
            )
        )
    if "ApplicationSnapshotConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_description

        out["application_snapshot_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_snapshot_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationSnapshotConfigurationDescription"]
            )
        )
    if "ApplicationSystemRollbackConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_description

        out["application_system_rollback_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_system_rollback_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationSystemRollbackConfigurationDescription"]
            )
        )
    if "VpcConfigurationDescriptions" in data:
        import aws_sdk_kinesis_analytics_v2.types.vpc_configuration_descriptions

        out["vpc_configuration_descriptions"] = (
            aws_sdk_kinesis_analytics_v2.types.vpc_configuration_descriptions.deserialize_aws_json_1_1(
                data["VpcConfigurationDescriptions"]
            )
        )
    if "ZeppelinApplicationConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_description

        out["zeppelin_application_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.zeppelin_application_configuration_description.deserialize_aws_json_1_1(
                data["ZeppelinApplicationConfigurationDescription"]
            )
        )
    if "ApplicationEncryptionConfigurationDescription" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description

        out["application_encryption_configuration_description"] = (
            aws_sdk_kinesis_analytics_v2.types.application_encryption_configuration_description.deserialize_aws_json_1_1(
                data["ApplicationEncryptionConfigurationDescription"]
            )
        )
    return out
