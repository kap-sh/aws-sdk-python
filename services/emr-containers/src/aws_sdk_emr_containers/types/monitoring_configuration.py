"""Generated from Smithy shape ``com.amazonaws.emrcontainers#MonitoringConfiguration``."""

from typing import TYPE_CHECKING, TypedDict

from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.cloud_watch_monitoring_configuration
    import aws_sdk_emr_containers.types.container_log_rotation_configuration
    import aws_sdk_emr_containers.types.managed_logs
    import aws_sdk_emr_containers.types.persistent_app_ui
    import aws_sdk_emr_containers.types.s3_monitoring_configuration


class MonitoringConfiguration(TypedDict):
    managed_logs: NotRequired["aws_sdk_emr_containers.types.managed_logs.ManagedLogs"]
    """<p>The entity that controls configuration for managed logs.</p>"""
    persistent_app_ui: NotRequired[
        "aws_sdk_emr_containers.types.persistent_app_ui.PersistentAppUI"
    ]
    """<p>Monitoring configurations for the persistent application UI. </p>"""
    cloud_watch_monitoring_configuration: NotRequired[
        "aws_sdk_emr_containers.types.cloud_watch_monitoring_configuration.CloudWatchMonitoringConfiguration"
    ]
    """<p>Monitoring configurations for CloudWatch.</p>"""
    s3_monitoring_configuration: NotRequired[
        "aws_sdk_emr_containers.types.s3_monitoring_configuration.S3MonitoringConfiguration"
    ]
    """<p>Amazon S3 configuration for monitoring log publishing.</p>"""
    container_log_rotation_configuration: NotRequired[
        "aws_sdk_emr_containers.types.container_log_rotation_configuration.ContainerLogRotationConfiguration"
    ]
    """<p>Enable or disable container log rotation.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MonitoringConfiguration) -> dict:
    out: dict = {}
    if "managed_logs" in value:
        import aws_sdk_emr_containers.types.managed_logs

        out["managedLogs"] = aws_sdk_emr_containers.types.managed_logs.serialize_json(
            value["managed_logs"]
        )
    if "persistent_app_ui" in value:
        import aws_sdk_emr_containers.types.persistent_app_ui

        out["persistentAppUI"] = (
            aws_sdk_emr_containers.types.persistent_app_ui.serialize_json(
                value["persistent_app_ui"]
            )
        )
    if "cloud_watch_monitoring_configuration" in value:
        import aws_sdk_emr_containers.types.cloud_watch_monitoring_configuration

        out["cloudWatchMonitoringConfiguration"] = (
            aws_sdk_emr_containers.types.cloud_watch_monitoring_configuration.serialize_json(
                value["cloud_watch_monitoring_configuration"]
            )
        )
    if "s3_monitoring_configuration" in value:
        import aws_sdk_emr_containers.types.s3_monitoring_configuration

        out["s3MonitoringConfiguration"] = (
            aws_sdk_emr_containers.types.s3_monitoring_configuration.serialize_json(
                value["s3_monitoring_configuration"]
            )
        )
    if "container_log_rotation_configuration" in value:
        import aws_sdk_emr_containers.types.container_log_rotation_configuration

        out["containerLogRotationConfiguration"] = (
            aws_sdk_emr_containers.types.container_log_rotation_configuration.serialize_json(
                value["container_log_rotation_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> MonitoringConfiguration:
    out: MonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "managedLogs" in data:
        import aws_sdk_emr_containers.types.managed_logs

        out["managed_logs"] = (
            aws_sdk_emr_containers.types.managed_logs.deserialize_json(
                data["managedLogs"]
            )
        )
    if "persistentAppUI" in data:
        import aws_sdk_emr_containers.types.persistent_app_ui

        out["persistent_app_ui"] = (
            aws_sdk_emr_containers.types.persistent_app_ui.deserialize_json(
                data["persistentAppUI"]
            )
        )
    if "cloudWatchMonitoringConfiguration" in data:
        import aws_sdk_emr_containers.types.cloud_watch_monitoring_configuration

        out["cloud_watch_monitoring_configuration"] = (
            aws_sdk_emr_containers.types.cloud_watch_monitoring_configuration.deserialize_json(
                data["cloudWatchMonitoringConfiguration"]
            )
        )
    if "s3MonitoringConfiguration" in data:
        import aws_sdk_emr_containers.types.s3_monitoring_configuration

        out["s3_monitoring_configuration"] = (
            aws_sdk_emr_containers.types.s3_monitoring_configuration.deserialize_json(
                data["s3MonitoringConfiguration"]
            )
        )
    if "containerLogRotationConfiguration" in data:
        import aws_sdk_emr_containers.types.container_log_rotation_configuration

        out["container_log_rotation_configuration"] = (
            aws_sdk_emr_containers.types.container_log_rotation_configuration.deserialize_json(
                data["containerLogRotationConfiguration"]
            )
        )
    return out
