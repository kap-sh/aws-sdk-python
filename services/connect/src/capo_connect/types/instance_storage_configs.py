"""Generated from Smithy shape ``com.amazonaws.connect#InstanceStorageConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_connect.types.instance_storage_config

InstanceStorageConfigs: TypeAlias = list[
    "capo_connect.types.instance_storage_config.InstanceStorageConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceStorageConfigs) -> list:
    import capo_connect.types.instance_storage_config

    out: list = []
    for item in value:
        out.append(capo_connect.types.instance_storage_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceStorageConfigs:
    import capo_connect.types.instance_storage_config

    out: InstanceStorageConfigs = []
    for item in data:
        out.append(capo_connect.types.instance_storage_config.deserialize_json(item))
    return out
