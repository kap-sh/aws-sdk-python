"""Generated from Smithy shape ``com.amazonaws.outposts#DetailedInstanceTypeListDefinition``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.detailed_instance_type_item

DetailedInstanceTypeListDefinition: TypeAlias = list[
    "aws_sdk_outposts.types.detailed_instance_type_item.DetailedInstanceTypeItem"
]


# --- restJson1 ser/de ---
def serialize_json(value: DetailedInstanceTypeListDefinition) -> list:
    import aws_sdk_outposts.types.detailed_instance_type_item

    out: list = []
    for item in value:
        out.append(
            aws_sdk_outposts.types.detailed_instance_type_item.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> DetailedInstanceTypeListDefinition:
    import aws_sdk_outposts.types.detailed_instance_type_item

    out: DetailedInstanceTypeListDefinition = []
    for item in data:
        out.append(
            aws_sdk_outposts.types.detailed_instance_type_item.deserialize_json(item)
        )
    return out
