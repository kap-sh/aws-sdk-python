"""Generated from Smithy shape ``com.amazonaws.novaact#Calls``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.call

Calls: TypeAlias = list["aws_sdk_nova_act.types.call.Call"]


# --- restJson1 ser/de ---
def serialize_json(value: Calls) -> list:
    import aws_sdk_nova_act.types.call

    out: list = []
    for item in value:
        out.append(aws_sdk_nova_act.types.call.serialize_json(item))
    return out


def deserialize_json(data: list) -> Calls:
    import aws_sdk_nova_act.types.call

    out: Calls = []
    for item in data:
        out.append(aws_sdk_nova_act.types.call.deserialize_json(item))
    return out
