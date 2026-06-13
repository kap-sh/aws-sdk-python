"""Generated from Smithy shape ``com.amazonaws.datazone#EnvironmentConfigurationUserParameter``."""

from typing import TYPE_CHECKING, TypedDict
from typing_extensions import NotRequired

if TYPE_CHECKING:
    import aws_sdk_datazone.types.environment_configuration_name
    import aws_sdk_datazone.types.environment_id
    import aws_sdk_datazone.types.environment_parameters_list
    import aws_sdk_datazone.types.environment_resolved_account


class EnvironmentConfigurationUserParameter(TypedDict):
    environment_id: NotRequired["aws_sdk_datazone.types.environment_id.EnvironmentId"]
    """<p>The ID of the environment.</p>"""
    environment_resolved_account: NotRequired[
        "aws_sdk_datazone.types.environment_resolved_account.EnvironmentResolvedAccount"
    ]
    """<p>Specifies the account/Region that is to be used during project creation for a particular blueprint.</p>"""
    environment_configuration_name: NotRequired[
        "aws_sdk_datazone.types.environment_configuration_name.EnvironmentConfigurationName"
    ]
    """<p>The environment configuration name.</p>"""
    environment_parameters: NotRequired[
        "aws_sdk_datazone.types.environment_parameters_list.EnvironmentParametersList"
    ]
    """<p>The environment parameters.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EnvironmentConfigurationUserParameter) -> dict:
    out: dict = {}
    if "environment_id" in value:
        out["environmentId"] = value["environment_id"]
    if "environment_resolved_account" in value:
        import aws_sdk_datazone.types.environment_resolved_account

        out["environmentResolvedAccount"] = (
            aws_sdk_datazone.types.environment_resolved_account.serialize_json(
                value["environment_resolved_account"]
            )
        )
    if "environment_configuration_name" in value:
        out["environmentConfigurationName"] = value["environment_configuration_name"]
    if "environment_parameters" in value:
        import aws_sdk_datazone.types.environment_parameters_list

        out["environmentParameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.serialize_json(
                value["environment_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> EnvironmentConfigurationUserParameter:
    out: EnvironmentConfigurationUserParameter = {}  # type: ignore[typeddict-item]
    if "environmentId" in data:
        out["environment_id"] = data["environmentId"]
    if "environmentResolvedAccount" in data:
        import aws_sdk_datazone.types.environment_resolved_account

        out["environment_resolved_account"] = (
            aws_sdk_datazone.types.environment_resolved_account.deserialize_json(
                data["environmentResolvedAccount"]
            )
        )
    if "environmentConfigurationName" in data:
        out["environment_configuration_name"] = data["environmentConfigurationName"]
    if "environmentParameters" in data:
        import aws_sdk_datazone.types.environment_parameters_list

        out["environment_parameters"] = (
            aws_sdk_datazone.types.environment_parameters_list.deserialize_json(
                data["environmentParameters"]
            )
        )
    return out
