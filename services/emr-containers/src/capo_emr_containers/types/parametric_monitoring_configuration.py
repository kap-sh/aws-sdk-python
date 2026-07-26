"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ParametricMonitoringConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.parametric_cloud_watch_monitoring_configuration
    import capo_emr_containers.types.parametric_s3_monitoring_configuration
    import capo_emr_containers.types.template_parameter


class ParametricMonitoringConfiguration(TypedDict, closed=True):
    persistent_app_ui: NotRequired[
        "capo_emr_containers.types.template_parameter.TemplateParameter"
    ]
    """<p> Monitoring configurations for the persistent application UI.</p>"""
    cloud_watch_monitoring_configuration: NotRequired[
        "capo_emr_containers.types.parametric_cloud_watch_monitoring_configuration.ParametricCloudWatchMonitoringConfiguration"
    ]
    """<p> Monitoring configurations for CloudWatch.</p>"""
    s3_monitoring_configuration: NotRequired[
        "capo_emr_containers.types.parametric_s3_monitoring_configuration.ParametricS3MonitoringConfiguration"
    ]
    """<p> Amazon S3 configuration for monitoring log publishing.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParametricMonitoringConfiguration) -> dict:
    out: dict = {}
    if "persistent_app_ui" in value:
        out["persistentAppUI"] = value["persistent_app_ui"]
    if "cloud_watch_monitoring_configuration" in value:
        import capo_emr_containers.types.parametric_cloud_watch_monitoring_configuration

        out["cloudWatchMonitoringConfiguration"] = (
            capo_emr_containers.types.parametric_cloud_watch_monitoring_configuration.serialize_json(
                value["cloud_watch_monitoring_configuration"]
            )
        )
    if "s3_monitoring_configuration" in value:
        import capo_emr_containers.types.parametric_s3_monitoring_configuration

        out["s3MonitoringConfiguration"] = (
            capo_emr_containers.types.parametric_s3_monitoring_configuration.serialize_json(
                value["s3_monitoring_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParametricMonitoringConfiguration:
    out: ParametricMonitoringConfiguration = {}  # type: ignore[typeddict-item]
    if "persistentAppUI" in data:
        out["persistent_app_ui"] = data["persistentAppUI"]
    if "cloudWatchMonitoringConfiguration" in data:
        import capo_emr_containers.types.parametric_cloud_watch_monitoring_configuration

        out["cloud_watch_monitoring_configuration"] = (
            capo_emr_containers.types.parametric_cloud_watch_monitoring_configuration.deserialize_json(
                data["cloudWatchMonitoringConfiguration"]
            )
        )
    if "s3MonitoringConfiguration" in data:
        import capo_emr_containers.types.parametric_s3_monitoring_configuration

        out["s3_monitoring_configuration"] = (
            capo_emr_containers.types.parametric_s3_monitoring_configuration.deserialize_json(
                data["s3MonitoringConfiguration"]
            )
        )
    return out
