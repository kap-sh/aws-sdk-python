"""Generated from Smithy shape ``com.amazonaws.qbusiness#Plugins``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_qbusiness.types.plugin

Plugins: TypeAlias = list["aws_sdk_qbusiness.types.plugin.Plugin"]


# --- restJson1 ser/de ---
def serialize_json(value: Plugins) -> list:
    import aws_sdk_qbusiness.types.plugin

    out: list = []
    for item in value:
        out.append(aws_sdk_qbusiness.types.plugin.serialize_json(item))
    return out


def deserialize_json(data: list) -> Plugins:
    import aws_sdk_qbusiness.types.plugin

    out: Plugins = []
    for item in data:
        out.append(aws_sdk_qbusiness.types.plugin.deserialize_json(item))
    return out
