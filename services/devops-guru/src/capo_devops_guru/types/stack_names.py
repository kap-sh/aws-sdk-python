"""Generated from Smithy shape ``com.amazonaws.devopsguru#StackNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.stack_name

StackNames: TypeAlias = list["capo_devops_guru.types.stack_name.StackName"]


# --- restJson1 ser/de ---
def serialize_json(value: StackNames) -> list:
    return list(value)


def deserialize_json(data: list) -> StackNames:
    return list(data)
