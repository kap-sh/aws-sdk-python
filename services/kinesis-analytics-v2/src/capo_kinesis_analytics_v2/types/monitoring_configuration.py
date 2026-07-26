"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#MonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_kinesis_analytics_v2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kinesis_analytics_v2.types.configuration_type
    import capo_kinesis_analytics_v2.types.log_level
    import capo_kinesis_analytics_v2.types.metrics_level


class MonitoringConfiguration(TypedDict, closed=True):
    configuration_type: (
        "capo_kinesis_analytics_v2.types.configuration_type.ConfigurationType"
    )
    """<p>Describes whether to use the default CloudWatch logging configuration for an application. You must set this property to <code>CUSTOM</code> in order to set the <code>LogLevel</code> or <code>MetricsLevel</code> parameters.</p>"""
    metrics_level: NotRequired[
        "capo_kinesis_analytics_v2.types.metrics_level.MetricsLevel"
    ]
    """<p>Describes the granularity of the CloudWatch Logs for an application. The <code>Parallelism</code> level is not recommended for applications with a Parallelism over 64 due to excessive costs.</p>"""
    log_level: NotRequired["capo_kinesis_analytics_v2.types.log_level.LogLevel"]
    """<p>Describes the verbosity of the CloudWatch Logs for an application.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MonitoringConfiguration) -> dict:
    out: dict = {}
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


def deserialize_aws_json_1_1(data: dict) -> MonitoringConfiguration:
    out: MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "ConfigurationType" in data:
        import capo_kinesis_analytics_v2.types.configuration_type

        out["configuration_type"] = (
            capo_kinesis_analytics_v2.types.configuration_type.deserialize_aws_json_1_1(
                data["ConfigurationType"]
            )
        )
    else:
        raise DeserializationError(
            "MonitoringConfiguration.configuration_type required"
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
