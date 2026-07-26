"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RunConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_restore_configuration
    import capo_kinesis_analytics_v2.types.flink_run_configuration
    import capo_kinesis_analytics_v2.types.sql_run_configurations


class RunConfiguration(TypedDict, closed=True):
    flink_run_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.flink_run_configuration.FlinkRunConfiguration"
    ]
    """<p>Describes the starting parameters for a Managed Service for Apache Flink application.</p>"""
    sql_run_configurations: NotRequired[
        "capo_kinesis_analytics_v2.types.sql_run_configurations.SqlRunConfigurations"
    ]
    """<p>Describes the starting parameters for a SQL-based Kinesis Data Analytics application application.</p>"""
    application_restore_configuration: NotRequired[
        "capo_kinesis_analytics_v2.types.application_restore_configuration.ApplicationRestoreConfiguration"
    ]
    """<p>Describes the restore behavior of a restarting application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunConfiguration) -> dict:
    out: dict = {}
    if "flink_run_configuration" in value:
        import capo_kinesis_analytics_v2.types.flink_run_configuration

        out["FlinkRunConfiguration"] = (
            capo_kinesis_analytics_v2.types.flink_run_configuration.serialize_aws_json_1_1(
                value["flink_run_configuration"]
            )
        )
    if "sql_run_configurations" in value:
        import capo_kinesis_analytics_v2.types.sql_run_configurations

        out["SqlRunConfigurations"] = (
            capo_kinesis_analytics_v2.types.sql_run_configurations.serialize_aws_json_1_1(
                value["sql_run_configurations"]
            )
        )
    if "application_restore_configuration" in value:
        import capo_kinesis_analytics_v2.types.application_restore_configuration

        out["ApplicationRestoreConfiguration"] = (
            capo_kinesis_analytics_v2.types.application_restore_configuration.serialize_aws_json_1_1(
                value["application_restore_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunConfiguration:
    out: RunConfiguration = {}  # type: ignore[typeddict-item]
    if "FlinkRunConfiguration" in data:
        import capo_kinesis_analytics_v2.types.flink_run_configuration

        out["flink_run_configuration"] = (
            capo_kinesis_analytics_v2.types.flink_run_configuration.deserialize_aws_json_1_1(
                data["FlinkRunConfiguration"]
            )
        )
    if "SqlRunConfigurations" in data:
        import capo_kinesis_analytics_v2.types.sql_run_configurations

        out["sql_run_configurations"] = (
            capo_kinesis_analytics_v2.types.sql_run_configurations.deserialize_aws_json_1_1(
                data["SqlRunConfigurations"]
            )
        )
    if "ApplicationRestoreConfiguration" in data:
        import capo_kinesis_analytics_v2.types.application_restore_configuration

        out["application_restore_configuration"] = (
            capo_kinesis_analytics_v2.types.application_restore_configuration.deserialize_aws_json_1_1(
                data["ApplicationRestoreConfiguration"]
            )
        )
    return out
