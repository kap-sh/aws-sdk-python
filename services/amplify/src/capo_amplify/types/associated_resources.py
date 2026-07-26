"""Generated from Smithy shape ``com.amazonaws.amplify#AssociatedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_amplify.types.associated_resource

AssociatedResources: TypeAlias = list[
    "capo_amplify.types.associated_resource.AssociatedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedResources) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociatedResources:
    return list(data)
