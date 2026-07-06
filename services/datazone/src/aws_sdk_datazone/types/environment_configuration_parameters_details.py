"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationParametersDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_configuration_parameters_list
    import aws_sdk_datazone.types.parameter_store_path


class EnvironmentConfigurationParametersDetails(TypedDict, closed=True):
    ssm_path: NotRequired[
        "aws_sdk_datazone.types.parameter_store_path.ParameterStorePath"
    ]
    """<p>Ssm path environment configuration parameters.</p>"""
    parameter_overrides: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_parameters_list.EnvironmentConfigurationParametersList"
    ]
    """<p>The parameter overrides.</p>"""
    resolved_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_parameters_list.EnvironmentConfigurationParametersList"
    ]
    """<p>The resolved environment configuration parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationParametersDetails) -> dict:
    out: dict = {}
    if "ssm_path" in value:
        out["ssmPath"] = value["ssm_path"]
    if "parameter_overrides" in value:
        import aws_sdk_datazone.types.environment_configuration_parameters_list

        out["parameterOverrides"] = (
            aws_sdk_datazone.types.environment_configuration_parameters_list.serialize_json(
                value["parameter_overrides"]
            )
        )
    if "resolved_parameters" in value:
        import aws_sdk_datazone.types.environment_configuration_parameters_list

        out["resolvedParameters"] = (
            aws_sdk_datazone.types.environment_configuration_parameters_list.serialize_json(
                value["resolved_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfigurationParametersDetails:
    out: EnvironmentConfigurationParametersDetails = {}  # type: ignore[typeddict-item]
    if "ssmPath" in data:
        out["ssm_path"] = data["ssmPath"]
    if "parameterOverrides" in data:
        import aws_sdk_datazone.types.environment_configuration_parameters_list

        out["parameter_overrides"] = (
            aws_sdk_datazone.types.environment_configuration_parameters_list.deserialize_json(
                data["parameterOverrides"]
            )
        )
    if "resolvedParameters" in data:
        import aws_sdk_datazone.types.environment_configuration_parameters_list

        out["resolved_parameters"] = (
            aws_sdk_datazone.types.environment_configuration_parameters_list.deserialize_json(
                data["resolvedParameters"]
            )
        )
    return out
