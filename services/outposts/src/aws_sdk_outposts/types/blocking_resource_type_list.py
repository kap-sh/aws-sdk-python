"""Generated from Smithy shape ``com.amazonaws.outposts#BlockingResourceTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_outposts.types.blocking_resource_type

BlockingResourceTypeList: TypeAlias = list[
    "aws_sdk_outposts.types.blocking_resource_type.BlockingResourceType"
]


# --- restJson1 ser/de ---
def serialize_json(value: BlockingResourceTypeList) -> list:
    import aws_sdk_outposts.types.blocking_resource_type

    out: list = []
    for item in value:
        out.append(aws_sdk_outposts.types.blocking_resource_type.serialize_json(item))
    return out


def deserialize_json(data: list) -> BlockingResourceTypeList:
    import aws_sdk_outposts.types.blocking_resource_type

    out: BlockingResourceTypeList = []
    for item in data:
        out.append(aws_sdk_outposts.types.blocking_resource_type.deserialize_json(item))
    return out
