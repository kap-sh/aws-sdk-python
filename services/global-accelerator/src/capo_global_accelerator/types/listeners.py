"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#Listeners``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.listener

Listeners: TypeAlias = list["capo_global_accelerator.types.listener.Listener"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Listeners) -> list:
    import capo_global_accelerator.types.listener

    out: list = []
    for item in value:
        out.append(capo_global_accelerator.types.listener.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> Listeners:
    import capo_global_accelerator.types.listener

    out: Listeners = []
    for item in data:
        out.append(
            capo_global_accelerator.types.listener.deserialize_aws_json_1_1(item)
        )
    return out
