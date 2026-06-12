"""Generated from Smithy shape ``com.amazonaws.novaact#CallResults``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_nova_act.types.call_result

CallResults: TypeAlias = list["aws_sdk_nova_act.types.call_result.CallResult"]


# --- restJson1 ser/de ---
def serialize_json(value: CallResults) -> list:
    import aws_sdk_nova_act.types.call_result

    out: list = []
    for item in value:
        out.append(aws_sdk_nova_act.types.call_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> CallResults:
    import aws_sdk_nova_act.types.call_result

    out: CallResults = []
    for item in data:
        out.append(aws_sdk_nova_act.types.call_result.deserialize_json(item))
    return out
