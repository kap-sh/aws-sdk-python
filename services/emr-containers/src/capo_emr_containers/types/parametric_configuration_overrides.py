"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ParametricConfigurationOverrides``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.configuration_list
    import capo_emr_containers.types.parametric_monitoring_configuration


class ParametricConfigurationOverrides(TypedDict, closed=True):
    application_configuration: NotRequired[
        "capo_emr_containers.types.configuration_list.ConfigurationList"
    ]
    """<p> The configurations for the application running by the job run.</p>"""
    monitoring_configuration: NotRequired[
        "capo_emr_containers.types.parametric_monitoring_configuration.ParametricMonitoringConfiguration"
    ]
    """<p> The configurations for monitoring. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ParametricConfigurationOverrides) -> dict:
    out: dict = {}
    if "application_configuration" in value:
        import capo_emr_containers.types.configuration_list

        out["applicationConfiguration"] = (
            capo_emr_containers.types.configuration_list.serialize_json(
                value["application_configuration"]
            )
        )
    if "monitoring_configuration" in value:
        import capo_emr_containers.types.parametric_monitoring_configuration

        out["monitoringConfiguration"] = (
            capo_emr_containers.types.parametric_monitoring_configuration.serialize_json(
                value["monitoring_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> ParametricConfigurationOverrides:
    out: ParametricConfigurationOverrides = {}  # type: ignore[typeddict-item]
    if "applicationConfiguration" in data:
        import capo_emr_containers.types.configuration_list

        out["application_configuration"] = (
            capo_emr_containers.types.configuration_list.deserialize_json(
                data["applicationConfiguration"]
            )
        )
    if "monitoringConfiguration" in data:
        import capo_emr_containers.types.parametric_monitoring_configuration

        out["monitoring_configuration"] = (
            capo_emr_containers.types.parametric_monitoring_configuration.deserialize_json(
                data["monitoringConfiguration"]
            )
        )
    return out
