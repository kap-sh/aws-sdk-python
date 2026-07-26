"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectEnvironmentEnvironmentVariablesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_securityhub.types.aws_code_build_project_environment_environment_variables_details

AwsCodeBuildProjectEnvironmentEnvironmentVariablesList: TypeAlias = list[
    "capo_securityhub.types.aws_code_build_project_environment_environment_variables_details.AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCodeBuildProjectEnvironmentEnvironmentVariablesList,
) -> list:
    import capo_securityhub.types.aws_code_build_project_environment_environment_variables_details

    out: list = []
    for item in value:
        out.append(
            capo_securityhub.types.aws_code_build_project_environment_environment_variables_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsCodeBuildProjectEnvironmentEnvironmentVariablesList:
    import capo_securityhub.types.aws_code_build_project_environment_environment_variables_details

    out: AwsCodeBuildProjectEnvironmentEnvironmentVariablesList = []
    for item in data:
        out.append(
            capo_securityhub.types.aws_code_build_project_environment_environment_variables_details.deserialize_json(
                item
            )
        )
    return out
