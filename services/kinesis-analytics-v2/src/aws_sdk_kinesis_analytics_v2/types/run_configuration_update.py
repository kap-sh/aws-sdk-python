"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RunConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.application_restore_configuration
    import aws_sdk_kinesis_analytics_v2.types.flink_run_configuration


class RunConfigurationUpdate(TypedDict):
    flink_run_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.flink_run_configuration.FlinkRunConfiguration"
    ]
    """<p>Describes the starting parameters for a Managed Service for Apache Flink application.</p>"""
    application_restore_configuration: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.application_restore_configuration.ApplicationRestoreConfiguration"
    ]
    """<p>Describes updates to the restore behavior of a restarting application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunConfigurationUpdate) -> dict:
    out: dict = {}
    if "flink_run_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.flink_run_configuration

        out["FlinkRunConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_run_configuration.serialize_aws_json_1_1(
                value["flink_run_configuration"]
            )
        )
    if "application_restore_configuration" in value:
        import aws_sdk_kinesis_analytics_v2.types.application_restore_configuration

        out["ApplicationRestoreConfiguration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_restore_configuration.serialize_aws_json_1_1(
                value["application_restore_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunConfigurationUpdate:
    out: RunConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "FlinkRunConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.flink_run_configuration

        out["flink_run_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.flink_run_configuration.deserialize_aws_json_1_1(
                data["FlinkRunConfiguration"]
            )
        )
    if "ApplicationRestoreConfiguration" in data:
        import aws_sdk_kinesis_analytics_v2.types.application_restore_configuration

        out["application_restore_configuration"] = (
            aws_sdk_kinesis_analytics_v2.types.application_restore_configuration.deserialize_aws_json_1_1(
                data["ApplicationRestoreConfiguration"]
            )
        )
    return out
