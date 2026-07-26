"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MonitoringConfigurationDescription``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.configuration_type
    import capo_kinesis_analytics_v2.types.log_level
    import capo_kinesis_analytics_v2.types.metrics_level


class MonitoringConfigurationDescription(TypedDict, closed=True):
    configuration_type: NotRequired[
        "capo_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    ]
    """<p>Describes whether to use the default CloudWatch logging configuration for an application.</p>"""
    metrics_level: NotRequired[
        "capo_kinesis_analytics_v2.types.metrics_level.MetricsLevel"
    ]
    """<p>Describes the granularity of the CloudWatch Logs for an application.</p>"""
    log_level: NotRequired["capo_kinesis_analytics_v2.types.log_level.LogLevel"]
    """<p>Describes the verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConfigurationDescription) -> dict:
    out: dict = {}
    if "configuration_type" in value:
        import capo_kinesis_analytics_v2.types.configuration_type

        out["ConfigurationType"] = (
            capo_kinesis_analytics_v2.types.configuration_type.serialize_aws_json_1_1(
                value["configuration_type"]
            )
        )
    if "metrics_level" in value:
        import capo_kinesis_analytics_v2.types.metrics_level

        out["MetricsLevel"] = (
            capo_kinesis_analytics_v2.types.metrics_level.serialize_aws_json_1_1(
                value["metrics_level"]
            )
        )
    if "log_level" in value:
        import capo_kinesis_analytics_v2.types.log_level

        out["LogLevel"] = (
            capo_kinesis_analytics_v2.types.log_level.serialize_aws_json_1_1(
                value["log_level"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> MonitoringConfigurationDescription:
    out: MonitoringConfigurationDescription = {}  # type: ignore[typeddict-item]
    if "ConfigurationType" in data:
        import capo_kinesis_analytics_v2.types.configuration_type

        out["configuration_type"] = (
            capo_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationType"]
            )
        )
    if "MetricsLevel" in data:
        import capo_kinesis_analytics_v2.types.metrics_level

        out["metrics_level"] = (
            capo_kinesis_analytics_v2.types.metrics_level.deserialize_aws_json_1_1(
                data["MetricsLevel"]
            )
        )
    if "LogLevel" in data:
        import capo_kinesis_analytics_v2.types.log_level

        out["log_level"] = (
            capo_kinesis_analytics_v2.types.log_level.deserialize_aws_json_1_1(
                data["LogLevel"]
            )
        )
    return out
