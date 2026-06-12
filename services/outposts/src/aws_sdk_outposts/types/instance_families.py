"""Generated from Smithy shape ``com.amazonaws.outposts#InstanceFamilies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.instance_family_name

InstanceFamilies: TypeAlias = list[
    "aws_sdk_outposts.types.instance_family_name.InstanceFamilyName"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceFamilies) -> list:
    return list(value)


def deserialize_json(data: list) -> InstanceFamilies:
    return list(data)
