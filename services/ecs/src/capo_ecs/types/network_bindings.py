"""Generated from Smithy shape ``com.amazonaws.ecs#NetworkBindings``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.network_binding

NetworkBindings: TypeAlias = list["capo_ecs.types.network_binding.NetworkBinding"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkBindings) -> list:
    import capo_ecs.types.network_binding

    out: list = []
    for item in value:
        out.append(capo_ecs.types.network_binding.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> NetworkBindings:
    import capo_ecs.types.network_binding

    out: NetworkBindings = []
    for item in data:
        out.append(capo_ecs.types.network_binding.deserialize_aws_json_1_1(item))
    return out
