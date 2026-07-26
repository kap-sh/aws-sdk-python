"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationParametersDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.environment_configuration_parameters_list
    import capo_datazone.types.parameter_store_path


class EnvironmentConfigurationParametersDetails(TypedDict, closed=True):
    ssm_path: NotRequired["capo_datazone.types.parameter_store_path.ParameterStorePath"]
    """<p>Ssm path environment configuration parameters.</p>"""
    parameter_overrides: NotRequired[
        "capo_datazone.types.environment_configuration_parameters_list.EnvironmentConfigurationParametersList"
    ]
    """<p>The parameter overrides.</p>"""
    resolved_parameters: NotRequired[
        "capo_datazone.types.environment_configuration_parameters_list.EnvironmentConfigurationParametersList"
    ]
    """<p>The resolved environment configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationParametersDetails) -> dict:
    out: dict = {}
    if "ssm_path" in value:
        out["ssmPath"] = value["ssm_path"]
    if "parameter_overrides" in value:
        import capo_datazone.types.environment_configuration_parameters_list

        out["parameterOverrides"] = (
            capo_datazone.types.environment_configuration_parameters_list.serialize_json(
                value["parameter_overrides"]
            )
        )
    if "resolved_parameters" in value:
        import capo_datazone.types.environment_configuration_parameters_list

        out["resolvedParameters"] = (
            capo_datazone.types.environment_configuration_parameters_list.serialize_json(
                value["resolved_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfigurationParametersDetails:
    out: EnvironmentConfigurationParametersDetails = {}  # type: ignore[typeddict-item]
    if "ssmPath" in data:
        out["ssm_path"] = data["ssmPath"]
    if "parameterOverrides" in data:
        import capo_datazone.types.environment_configuration_parameters_list

        out["parameter_overrides"] = (
            capo_datazone.types.environment_configuration_parameters_list.deserialize_json(
                data["parameterOverrides"]
            )
        )
    if "resolvedParameters" in data:
        import capo_datazone.types.environment_configuration_parameters_list

        out["resolved_parameters"] = (
            capo_datazone.types.environment_configuration_parameters_list.deserialize_json(
                data["resolvedParameters"]
            )
        )
    return out
