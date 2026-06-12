"""Generated from Smithy shape ``com.amazonaws.resiliencehub#PhysicalResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.physical_resource

PhysicalResourceList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.physical_resource.PhysicalResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalResourceList) -> list:
    import aws_sdk_resiliencehub.types.physical_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.physical_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> PhysicalResourceList:
    import aws_sdk_resiliencehub.types.physical_resource

    out: PhysicalResourceList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.physical_resource.deserialize_json(item))
    return out
