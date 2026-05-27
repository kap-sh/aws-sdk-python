"""Generated from Smithy shape ``com.amazonaws.ecs#CapacityProviderFieldList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ecs.types.capacity_provider_field

CapacityProviderFieldList: TypeAlias = list[
    "aws_sdk_ecs.types.capacity_provider_field.CapacityProviderField"
]
