"""Generated from Smithy shape ``com.amazonaws.globalaccelerator#CustomRoutingAccelerators``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_global_accelerator.types.custom_routing_accelerator

CustomRoutingAccelerators: TypeAlias = list[
    "capo_global_accelerator.types.custom_routing_accelerator.CustomRoutingAccelerator"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomRoutingAccelerators) -> list:
    import capo_global_accelerator.types.custom_routing_accelerator

    out: list = []
    for item in value:
        out.append(
            capo_global_accelerator.types.custom_routing_accelerator.serialize_aws_json_1_1(
                item
            )
        )
    return out


def deserialize_aws_json_1_1(data: list) -> CustomRoutingAccelerators:
    import capo_global_accelerator.types.custom_routing_accelerator

    out: CustomRoutingAccelerators = []
    for item in data:
        out.append(
            capo_global_accelerator.types.custom_routing_accelerator.deserialize_aws_json_1_1(
                item
            )
        )
    return out
