"""Generated from Smithy shape ``com.amazonaws.devopsguru#EventResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_devops_guru.types.event_resource

EventResources: TypeAlias = list[
    "aws_sdk_devops_guru.types.event_resource.EventResource"
]


# --- restJson1 ser/de ---
def serialize_json(value: EventResources) -> list:
    import aws_sdk_devops_guru.types.event_resource

    out: list = []
    for item in value:
        out.append(aws_sdk_devops_guru.types.event_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> EventResources:
    import aws_sdk_devops_guru.types.event_resource

    out: EventResources = []
    for item in data:
        out.append(aws_sdk_devops_guru.types.event_resource.deserialize_json(item))
    return out
