"""Generated from Smithy shape ``com.amazonaws.controlcatalog#GovernedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_controlcatalog.types.governed_resource

GovernedResources: TypeAlias = list[
    "aws_sdk_controlcatalog.types.governed_resource.GovernedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: GovernedResources) -> list:
    return list(value)


def deserialize_json(data: list) -> GovernedResources:
    return list(data)
