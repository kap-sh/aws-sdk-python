"""Generated from Smithy shape ``com.amazonaws.codepipeline#EnvironmentVariableList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_codepipeline.types.environment_variable

EnvironmentVariableList: TypeAlias = list[
    "capo_codepipeline.types.environment_variable.EnvironmentVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariableList) -> list:
    import capo_codepipeline.types.environment_variable

    out: list = []
    for item in value:
        out.append(
            capo_codepipeline.types.environment_variable.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentVariableList:
    import capo_codepipeline.types.environment_variable

    out: EnvironmentVariableList = []
    for item in data:
        out.append(
            capo_codepipeline.types.environment_variable.deserialize_aws_json_1_1(item)
        )
    return out
