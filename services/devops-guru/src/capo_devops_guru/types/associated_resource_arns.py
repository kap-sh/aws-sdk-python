"""Generated from Smithy shape ``com.amazonaws.devopsguru#AssociatedResourceArns``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.resource_arn

AssociatedResourceArns: TypeAlias = list[
    "capo_devops_guru.types.resource_arn.ResourceArn"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedResourceArns) -> list:
    return list(value)


def deserialize_json(data: list) -> AssociatedResourceArns:
    return list(data)
