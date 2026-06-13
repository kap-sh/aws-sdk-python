"""Generated from Smithy shape ``com.amazonaws.evs#EnvironmentStateList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_evs.types.environment_state

EnvironmentStateList: TypeAlias = list[
    "aws_sdk_evs.types.environment_state.EnvironmentState"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentStateList) -> list:
    import aws_sdk_evs.types.environment_state

    out: list = []
    for item in value:
        out.append(aws_sdk_evs.types.environment_state.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentStateList:
    import aws_sdk_evs.types.environment_state

    out: EnvironmentStateList = []
    for item in data:
        out.append(aws_sdk_evs.types.environment_state.deserialize_aws_json_1_0(item))
    return out
