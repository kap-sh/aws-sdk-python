"""Generated from Smithy shape ``com.amazonaws.guardduty#Containers``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_guardduty.types.container

Containers: TypeAlias = list["aws_sdk_guardduty.types.container.Container"]


# --- restJson1 ser/de ---
def serialize_json(value: Containers) -> list:
    import aws_sdk_guardduty.types.container

    out: list = []
    for item in value:
        out.append(aws_sdk_guardduty.types.container.serialize_json(item))
    return out


def deserialize_json(data: list) -> Containers:
    import aws_sdk_guardduty.types.container

    out: Containers = []
    for item in data:
        out.append(aws_sdk_guardduty.types.container.deserialize_json(item))
    return out
