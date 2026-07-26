"""Generated from Smithy shape ``com.amazonaws.outposts#InstanceTypeListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_outposts.types.instance_type_item

InstanceTypeListDefinition: TypeAlias = list[
    "capo_outposts.types.instance_type_item.InstanceTypeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: InstanceTypeListDefinition) -> list:
    import capo_outposts.types.instance_type_item

    out: list = []
    for item in value:
        out.append(capo_outposts.types.instance_type_item.serialize_json(item))
    return out


def deserialize_json(data: list) -> InstanceTypeListDefinition:
    import capo_outposts.types.instance_type_item

    out: InstanceTypeListDefinition = []
    for item in data:
        out.append(capo_outposts.types.instance_type_item.deserialize_json(item))
    return out
