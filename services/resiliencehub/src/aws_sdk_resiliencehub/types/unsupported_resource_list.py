"""Generated from Smithy shape ``com.amazonaws.resiliencehub#UnsupportedResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.unsupported_resource

UnsupportedResourceList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.unsupported_resource.UnsupportedResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: UnsupportedResourceList) -> list:
    import aws_sdk_resiliencehub.types.unsupported_resource

    out: list = []
    for item in value:
        out.append(
            aws_sdk_resiliencehub.types.unsupported_resource.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> UnsupportedResourceList:
    import aws_sdk_resiliencehub.types.unsupported_resource

    out: UnsupportedResourceList = []
    for item in data:
        out.append(
            aws_sdk_resiliencehub.types.unsupported_resource.deserialize_json(item)
        )
    return out
