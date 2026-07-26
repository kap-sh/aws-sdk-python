"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviders``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.capacity_provider

CapacityProviders: TypeAlias = list["capo_ecs.types.capacity_provider.CapacityProvider"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviders) -> list:
    import capo_ecs.types.capacity_provider

    out: list = []
    for item in value:
        out.append(capo_ecs.types.capacity_provider.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CapacityProviders:
    import capo_ecs.types.capacity_provider

    out: CapacityProviders = []
    for item in data:
        out.append(capo_ecs.types.capacity_provider.deserialize_aws_json_1_1(item))
    return out
