"""Generated from Smithy shape ``com.amazonaws.synthetics#EngineConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.engine_config

EngineConfigs: TypeAlias = list["aws_sdk_synthetics.types.engine_config.EngineConfig"]


# --- restJson1 ser/de ---
def serialize_json(value: EngineConfigs) -> list:
    import aws_sdk_synthetics.types.engine_config

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.engine_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> EngineConfigs:
    import aws_sdk_synthetics.types.engine_config

    out: EngineConfigs = []
    for item in data:
        out.append(aws_sdk_synthetics.types.engine_config.deserialize_json(item))
    return out
