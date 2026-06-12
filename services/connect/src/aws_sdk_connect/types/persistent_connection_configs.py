"""Generated from Smithy shape ``com.amazonaws.connect#PersistentConnectionConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_connect.types.persistent_connection_config

PersistentConnectionConfigs: TypeAlias = list[
    "aws_sdk_connect.types.persistent_connection_config.PersistentConnectionConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: PersistentConnectionConfigs) -> list:
    import aws_sdk_connect.types.persistent_connection_config

    out: list = []
    for item in value:
        out.append(
            aws_sdk_connect.types.persistent_connection_config.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> PersistentConnectionConfigs:
    import aws_sdk_connect.types.persistent_connection_config

    out: PersistentConnectionConfigs = []
    for item in data:
        out.append(
            aws_sdk_connect.types.persistent_connection_config.deserialize_json(item)
        )
    return out
