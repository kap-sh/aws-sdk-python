"""Generated from Smithy shape ``com.amazonaws.devopsguru#UpdateStackNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_devops_guru.types.stack_name

UpdateStackNames: TypeAlias = list["capo_devops_guru.types.stack_name.StackName"]


# --- restJson1 ser/de ---
def serialize_json(value: UpdateStackNames) -> list:
    return list(value)


def deserialize_json(data: list) -> UpdateStackNames:
    return list(data)
