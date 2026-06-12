"""Generated from Smithy shape ``com.amazonaws.securityhub#AwsCodeBuildProjectEnvironmentEnvironmentVariablesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_details

AwsCodeBuildProjectEnvironmentEnvironmentVariablesList: TypeAlias = list[
    "aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_details.AwsCodeBuildProjectEnvironmentEnvironmentVariablesDetails"
]


# --- restJson1 ser/de ---
def serialize_json(
    value: AwsCodeBuildProjectEnvironmentEnvironmentVariablesList,
) -> list:
    import aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_details

    out: list = []
    for item in value:
        out.append(
            aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_details.serialize_json(
                item
            )
        )
    return out


def deserialize_json(
    data: list,
) -> AwsCodeBuildProjectEnvironmentEnvironmentVariablesList:
    import aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_details

    out: AwsCodeBuildProjectEnvironmentEnvironmentVariablesList = []
    for item in data:
        out.append(
            aws_sdk_securityhub.types.aws_code_build_project_environment_environment_variables_details.deserialize_json(
                item
            )
        )
    return out
