"""Generated from Smithy shape ``com.amazonaws.deadline#InstanceTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_deadline.types.instance_type

InstanceTypes: TypeAlias = list["capo_deadline.types.instance_type.InstanceType"]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypes) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceTypes:
    return list(data)
