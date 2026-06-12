"""Generated from Smithy shape ``com.amazonaws.networkmanager#PathComponentList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.path_component

PathComponentList: TypeAlias = list[
    "aws_sdk_networkmanager.types.path_component.PathComponent"
]


# --- restJson1 ser/de ---
def serialize_json(value: PathComponentList) -> list:
    import aws_sdk_networkmanager.types.path_component

    out: list = []
    for item in value:
        out.append(aws_sdk_networkmanager.types.path_component.serialize_json(item))
    return out


def deserialize_json(data: list) -> PathComponentList:
    import aws_sdk_networkmanager.types.path_component

    out: PathComponentList = []
    for item in data:
        out.append(aws_sdk_networkmanager.types.path_component.deserialize_json(item))
    return out
