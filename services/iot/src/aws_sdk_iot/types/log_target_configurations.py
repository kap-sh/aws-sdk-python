"""Generated from Smithy shape ``com.amazonaws.iot#LogTargetConfigurations``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_iot.types.log_target_configuration

LogTargetConfigurations: TypeAlias = list[
    "aws_sdk_iot.types.log_target_configuration.LogTargetConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: LogTargetConfigurations) -> list:
    import aws_sdk_iot.types.log_target_configuration

    out: list = []
    for item in value:
        out.append(aws_sdk_iot.types.log_target_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> LogTargetConfigurations:
    import aws_sdk_iot.types.log_target_configuration

    out: LogTargetConfigurations = []
    for item in data:
        out.append(aws_sdk_iot.types.log_target_configuration.deserialize_json(item))
    return out
