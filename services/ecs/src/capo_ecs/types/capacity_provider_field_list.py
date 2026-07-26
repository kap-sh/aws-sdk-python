"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_ecs.types.capacity_provider_field

CapacityProviderFieldList: TypeAlias = list[
    "capo_ecs.types.capacity_provider_field.CapacityProviderField"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CapacityProviderFieldList) -> list:
    import capo_ecs.types.capacity_provider_field

    out: list = []
    for item in value:
        out.append(capo_ecs.types.capacity_provider_field.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CapacityProviderFieldList:
    import capo_ecs.types.capacity_provider_field

    out: CapacityProviderFieldList = []
    for item in data:
        out.append(
            capo_ecs.types.capacity_provider_field.deserialize_aws_json_1_1(item)
        )
    return out
