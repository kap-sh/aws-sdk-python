"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogsConfigurationPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_cleanroomsml.types.logs_configuration_policy

LogsConfigurationPolicyList: TypeAlias = list[
    "aws_sdk_cleanroomsml.types.logs_configuration_policy.LogsConfigurationPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogsConfigurationPolicyList) -> list:
    import aws_sdk_cleanroomsml.types.logs_configuration_policy

    out: list = []
    for item in value:
        out.append(
            aws_sdk_cleanroomsml.types.logs_configuration_policy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LogsConfigurationPolicyList:
    import aws_sdk_cleanroomsml.types.logs_configuration_policy

    out: LogsConfigurationPolicyList = []
    for item in data:
        out.append(
            aws_sdk_cleanroomsml.types.logs_configuration_policy.deserialize_json(item)
        )
    return out
