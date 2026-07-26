"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#LogsConfigurationPolicyList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_cleanroomsml.types.logs_configuration_policy

LogsConfigurationPolicyList: TypeAlias = list[
    "capo_cleanroomsml.types.logs_configuration_policy.LogsConfigurationPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogsConfigurationPolicyList) -> list:
    import capo_cleanroomsml.types.logs_configuration_policy

    out: list = []
    for item in value:
        out.append(
            capo_cleanroomsml.types.logs_configuration_policy.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> LogsConfigurationPolicyList:
    import capo_cleanroomsml.types.logs_configuration_policy

    out: LogsConfigurationPolicyList = []
    for item in data:
        out.append(
            capo_cleanroomsml.types.logs_configuration_policy.deserialize_json(item)
        )
    return out
