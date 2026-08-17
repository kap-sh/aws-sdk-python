"""Generated from Smithy shape ``com.amazonaws.ecs#EnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.key_value_pair

EnvironmentVariables: TypeAlias = list["capo_ecs.types.key_value_pair.KeyValuePair"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariables) -> list:
    import capo_ecs.types.key_value_pair

    out: list = []
    for item in value:
        out.append(capo_ecs.types.key_value_pair.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentVariables:
    import capo_ecs.types.key_value_pair

    out: EnvironmentVariables = []
    for item in data:
        if item is None:
            continue
        out.append(capo_ecs.types.key_value_pair.deserialize_aws_json_1_1(item))
    return out
