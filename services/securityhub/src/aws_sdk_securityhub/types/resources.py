"""Generated from Smithy shape ``com.amazonaws.securityhub#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_securityhub.types.resource_result

Resources: TypeAlias = list["aws_sdk_securityhub.types.resource_result.ResourceResult"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    import aws_sdk_securityhub.types.resource_result

    out: list = []
    for item in value:
        out.append(aws_sdk_securityhub.types.resource_result.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resources:
    import aws_sdk_securityhub.types.resource_result

    out: Resources = []
    for item in data:
        out.append(aws_sdk_securityhub.types.resource_result.deserialize_json(item))
    return out
