"""Generated from Smithy shape ``com.amazonaws.emrserverless#MonitoringConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_serverless.types.cloud_watch_logging_configuration
    import aws_sdk_emr_serverless.types.managed_persistence_monitoring_configuration
    import aws_sdk_emr_serverless.types.prometheus_monitoring_configuration
    import aws_sdk_emr_serverless.types.s3_monitoring_configuration


class MonitoringConfiguration(TypedDict):
    s3_monitoring_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.s3_monitoring_configuration.S3MonitoringConfiguration"
    ]
    """<p>The Amazon S3 configuration for monitoring log publishing.</p>"""
    managed_persistence_monitoring_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.managed_persistence_monitoring_configuration.ManagedPersistenceMonitoringConfiguration"
    ]
    """<p>The managed log persistence configuration for a job run.</p>"""
    cloud_watch_logging_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.cloud_watch_logging_configuration.CloudWatchLoggingConfiguration"
    ]
    """<p>The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.</p>"""
    prometheus_monitoring_configuration: NotRequired[
        "aws_sdk_emr_serverless.types.prometheus_monitoring_configuration.PrometheusMonitoringConfiguration"
    ]
    """<p>The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitoringConfiguration) -> dict:
    out: dict = {}
    if "s3_monitoring_configuration" in value:
        import aws_sdk_emr_serverless.types.s3_monitoring_configuration

        out["s3MonitoringConfiguration"] = (
            aws_sdk_emr_serverless.types.s3_monitoring_configuration.serialize_json(
                value["s3_monitoring_configuration"]
            )
        )
    if "managed_persistence_monitoring_configuration" in value:
        import aws_sdk_emr_serverless.types.managed_persistence_monitoring_configuration

        out["managedPersistenceMonitoringConfiguration"] = (
            aws_sdk_emr_serverless.types.managed_persistence_monitoring_configuration.serialize_json(
                value["managed_persistence_monitoring_configuration"]
            )
        )
    if "cloud_watch_logging_configuration" in value:
        import aws_sdk_emr_serverless.types.cloud_watch_logging_configuration

        out["cloudWatchLoggingConfiguration"] = (
            aws_sdk_emr_serverless.types.cloud_watch_logging_configuration.serialize_json(
                value["cloud_watch_logging_configuration"]
            )
        )
    if "prometheus_monitoring_configuration" in value:
        import aws_sdk_emr_serverless.types.prometheus_monitoring_configuration

        out["prometheusMonitoringConfiguration"] = (
            aws_sdk_emr_serverless.types.prometheus_monitoring_configuration.serialize_json(
                value["prometheus_monitoring_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitoringConfiguration:
    out: MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "s3MonitoringConfiguration" in data:
        import aws_sdk_emr_serverless.types.s3_monitoring_configuration

        out["s3_monitoring_configuration"] = (
            aws_sdk_emr_serverless.types.s3_monitoring_configuration.deserialize_json(
                data["s3MonitoringConfiguration"]
            )
        )
    if "managedPersistenceMonitoringConfiguration" in data:
        import aws_sdk_emr_serverless.types.managed_persistence_monitoring_configuration

        out["managed_persistence_monitoring_configuration"] = (
            aws_sdk_emr_serverless.types.managed_persistence_monitoring_configuration.deserialize_json(
                data["managedPersistenceMonitoringConfiguration"]
            )
        )
    if "cloudWatchLoggingConfiguration" in data:
        import aws_sdk_emr_serverless.types.cloud_watch_logging_configuration

        out["cloud_watch_logging_configuration"] = (
            aws_sdk_emr_serverless.types.cloud_watch_logging_configuration.deserialize_json(
                data["cloudWatchLoggingConfiguration"]
            )
        )
    if "prometheusMonitoringConfiguration" in data:
        import aws_sdk_emr_serverless.types.prometheus_monitoring_configuration

        out["prometheus_monitoring_configuration"] = (
            aws_sdk_emr_serverless.types.prometheus_monitoring_configuration.deserialize_json(
                data["prometheusMonitoringConfiguration"]
            )
        )
    return out
