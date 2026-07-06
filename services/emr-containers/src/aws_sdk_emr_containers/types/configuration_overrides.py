"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ConfigurationOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_emr_containers.types.configuration_list
    import aws_sdk_emr_containers.types.monitoring_configuration


class ConfigurationOverrides(TypedDict, closed=True):
    application_configuration: NotRequired[
        "aws_sdk_emr_containers.types.configuration_list.ConfigurationList"
    ]
    """<p>The configurations for the application running by the job run. </p>"""
    monitoring_configuration: NotRequired[
        "aws_sdk_emr_containers.types.monitoring_configuration.MonitoringConfiguration"
    ]
    """<p>The configurations for monitoring.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ConfigurationOverrides) -> dict:
    out: dict = {}
    if "application_configuration" in value:
        import aws_sdk_emr_containers.types.configuration_list

        out["applicationConfiguration"] = (
            aws_sdk_emr_containers.types.configuration_list.serialize_json(
                value["application_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import aws_sdk_emr_containers.types.monitoring_configuration

        out["monitoringConfiguration"] = (
            aws_sdk_emr_containers.types.monitoring_configuration.serialize_json(
                value["monitoring_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ConfigurationOverrides:
    out: ConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if "applicationConfiguration" in data:
        import aws_sdk_emr_containers.types.configuration_list

        out["application_configuration"] = (
            aws_sdk_emr_containers.types.configuration_list.deserialize_json(
                data["applicationConfiguration"]
            )
        )
    if "monitoringConfiguration" in data:
        import aws_sdk_emr_containers.types.monitoring_configuration

        out["monitoring_configuration"] = (
            aws_sdk_emr_containers.types.monitoring_configuration.deserialize_json(
                data["monitoringConfiguration"]
            )
        )
    return out
