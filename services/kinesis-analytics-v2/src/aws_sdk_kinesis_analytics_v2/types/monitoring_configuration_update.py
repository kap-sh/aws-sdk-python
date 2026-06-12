"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MonitoringConfigurationUpdate``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_kinesis_analytics_v2.types.configuration_type
    import aws_sdk_kinesis_analytics_v2.types.log_level
    import aws_sdk_kinesis_analytics_v2.types.metrics_level


class MonitoringConfigurationUpdate(TypedDict):
    configuration_type_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    ]
    """<p>Describes updates to whether to use the default CloudWatch logging configuration for an application. You must set this property to <code>CUSTOM</code> in order to set the <code>LogLevel</code> or <code>MetricsLevel</code> parameters.</p>"""
    metrics_level_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.metrics_level.MetricsLevel"
    ]
    """<p>Describes updates to the granularity of the CloudWatch Logs for an application. The <code>Parallelism</code> level is not recommended for applications with a Parallelism over 64 due to excessive costs.</p>"""
    log_level_update: NotRequired[
        "aws_sdk_kinesis_analytics_v2.types.log_level.LogLevel"
    ]
    """<p>Describes updates to the verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConfigurationUpdate) -> dict:
    out: dict = {}
    if "configuration_type_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["ConfigurationTypeUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
                value["configuration_type_update"]
            )
        )
    if "metrics_level_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.metrics_level

        out["MetricsLevelUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.metrics_level.serialize_aws_json_1_1(
                value["metrics_level_update"]
            )
        )
    if "log_level_update" in value:
        import aws_sdk_kinesis_analytics_v2.types.log_level

        out["LogLevelUpdate"] = (
            aws_sdk_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
                value["log_level_update"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringConfigurationUpdate:
    out: MonitoringConfigurationUpdate = {}  # type: ignore[typeddict-item]
    if "ConfigurationTypeUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.configuration_type

        out["configuration_type_update"] = (
            aws_sdk_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationTypeUpdate"]
            )
        )
    if "MetricsLevelUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.metrics_level

        out["metrics_level_update"] = (
            aws_sdk_kinesis_analytics_v2.types.metrics_level.deserialize_aws_json_1_1(
                data["MetricsLevelUpdate"]
            )
        )
    if "LogLevelUpdate" in data:
        import aws_sdk_kinesis_analytics_v2.types.log_level

        out["log_level_update"] = (
            aws_sdk_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevelUpdate"]
            )
        )
    return out
