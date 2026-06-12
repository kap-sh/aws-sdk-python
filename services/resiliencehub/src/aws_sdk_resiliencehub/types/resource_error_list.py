"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ResourceErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_resiliencehub.types.resource_error

ResourceErrorList: TypeAlias = list[
    "aws_sdk_resiliencehub.types.resource_error.ResourceError"
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceErrorList) -> list:
    import aws_sdk_resiliencehub.types.resource_error

    out: list = []
    for item in value:
        out.append(aws_sdk_resiliencehub.types.resource_error.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceErrorList:
    import aws_sdk_resiliencehub.types.resource_error

    out: ResourceErrorList = []
    for item in data:
        out.append(aws_sdk_resiliencehub.types.resource_error.deserialize_json(item))
    return out
