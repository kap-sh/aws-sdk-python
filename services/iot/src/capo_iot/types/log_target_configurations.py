"""Generated from Smithy shape ``com.amazonaws.iot#LogTargetConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.log_target_configuration

LogTargetConfigurations: TypeAlias = list[
    "capo_iot.types.log_target_configuration.LogTargetConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogTargetConfigurations) -> list:
    import capo_iot.types.log_target_configuration

    out: list = []
    for item in value:
        out.append(capo_iot.types.log_target_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogTargetConfigurations:
    import capo_iot.types.log_target_configuration

    out: LogTargetConfigurations = []
    for item in data:
        out.append(capo_iot.types.log_target_configuration.deserialize_json(item))
    return out
