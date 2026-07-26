"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#RunConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.application_restore_configuration
    import capo_kinesis_analytics_v2.types.flink_run_configuration


class RunConfigurationDescription(TypedDict, closed=True):
    application_restore_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.application_restore_configuration.ApplicationRestoreConfiguration"
    ]
    """<p>Describes the restore behavior of a restarting application.</p>"""
    flink_run_configuration_description: NotRequired[
        "capo_kinesis_analytics_v2.types.flink_run_configuration.FlinkRunConfiguration"
    ]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RunConfigurationDescription) -> dict:
    out: dict = {}
    if "application_restore_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.application_restore_configuration

        out["ApplicationRestoreConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.application_restore_configuration.serialize_aws_json_1_1(
                value["application_restore_configuration_description"]
            )
        )
    if "flink_run_configuration_description" in value:
        import capo_kinesis_analytics_v2.types.flink_run_configuration

        out["FlinkRunConfigurationDescription"] = (
            capo_kinesis_analytics_v2.types.flink_run_configuration.serialize_aws_json_1_1(
                value["flink_run_configuration_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> RunConfigurationDescription:
    out: RunConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "ApplicationRestoreConfigurationDescription" in data:
        import capo_kinesis_analytics_v2.types.application_restore_configuration

        out["application_restore_configuration_description"] = (
            capo_kinesis_analytics_v2.types.application_restore_configuration.deserialize_aws_json_1_1(
                data["ApplicationRestoreConfigurationDescription"]
            )
        )
    if "FlinkRunConfigurationDescription" in data:
        import capo_kinesis_analytics_v2.types.flink_run_configuration

        out["flink_run_configuration_description"] = (
            capo_kinesis_analytics_v2.types.flink_run_configuration.deserialize_aws_json_1_1(
                data["FlinkRunConfigurationDescription"]
            )
        )
    return out
