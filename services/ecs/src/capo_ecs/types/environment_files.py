"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentFiles``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.environment_file

EnvironmentFiles: TypeAlias = list["capo_ecs.types.environment_file.EnvironmentFile"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentFiles) -> list:
    import capo_ecs.types.environment_file

    out: list = []
    for item in value:
        out.append(capo_ecs.types.environment_file.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentFiles:
    import capo_ecs.types.environment_file

    out: EnvironmentFiles = []
    for item in data:
        out.append(capo_ecs.types.environment_file.deserialize_aws_json_1_1(item))
    return out
