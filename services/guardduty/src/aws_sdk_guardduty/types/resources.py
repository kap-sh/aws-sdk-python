"""Generated from Smithy shape ``com.amazonaws.guardduty#Resources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.resource_v2

Resources: TypeAlias = list["aws_sdk_guardduty.types.resource_v2.ResourceV2"]


# --- restJson1 ser/de ---
def serialize_json(value: Resources) -> list:
    import aws_sdk_guardduty.types.resource_v2

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.resource_v2.serialize_json(item))
    return out


def deserialize_json(data: list) -> Resources:
    import aws_sdk_guardduty.types.resource_v2

    out: Resources = []
    for item in data:
        out.append(aws_sdk_guardduty.types.resource_v2.deserialize_json(item))
    return out
