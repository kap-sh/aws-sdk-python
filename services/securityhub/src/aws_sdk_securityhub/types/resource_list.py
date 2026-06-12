"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resource

ResourceList: TypeAlias = list["aws_sdk_securityhub.types.resource.Resource"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    import aws_sdk_securityhub.types.resource

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceList:
    import aws_sdk_securityhub.types.resource

    out: ResourceList = []
    for item in data:
        out.append(aws_sdk_securityhub.types.resource.deserialize_json(item))
    return out
