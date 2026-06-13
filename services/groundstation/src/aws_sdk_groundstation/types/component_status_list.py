"""Generated from Smithy shape ``com.amazonaws.groundstation#ComponentStatusList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_groundstation.types.component_status_data

ComponentStatusList: TypeAlias = list[
    "aws_sdk_groundstation.types.component_status_data.ComponentStatusData"
]


# --- restJson1 ser/de ---
def serialize_json(value: ComponentStatusList) -> list:
    import aws_sdk_groundstation.types.component_status_data

    out: list = []
    for item in value:
        out.append(
            aws_sdk_groundstation.types.component_status_data.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> ComponentStatusList:
    import aws_sdk_groundstation.types.component_status_data

    out: ComponentStatusList = []
    for item in data:
        out.append(
            aws_sdk_groundstation.types.component_status_data.deserialize_json(item)
        )
    return out
