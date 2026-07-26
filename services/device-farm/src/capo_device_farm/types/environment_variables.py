"""Generated from Smithy shape ``com.amazonaws.devicefarm#EnvironmentVariables``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_device_farm.types.environment_variable

EnvironmentVariables: TypeAlias = list[
    "capo_device_farm.types.environment_variable.EnvironmentVariable"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EnvironmentVariables) -> list:
    import capo_device_farm.types.environment_variable

    out: list = []
    for item in value:
        out.append(
            capo_device_farm.types.environment_variable.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EnvironmentVariables:
    import capo_device_farm.types.environment_variable

    out: EnvironmentVariables = []
    for item in data:
        out.append(
            capo_device_farm.types.environment_variable.deserialize_aws_json_1_1(item)
        )
    return out
