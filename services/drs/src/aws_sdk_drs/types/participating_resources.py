"""Generated from Smithy shape ``com.amazonaws.drs#ParticipatingResources``."""

from typing import TYPE_CHECKING, TypeAlias
if TYPE_CHECKING:
    import aws_sdk_drs.types.participating_resource

ParticipatingResources: TypeAlias = list["aws_sdk_drs.types.participating_resource.ParticipatingResource"]


# --- restJson1 ser/de ---
def serialize_json(value: ParticipatingResources) -> list:
    import aws_sdk_drs.types.participating_resource
    out: list = []
    for item in value:
        out.append(aws_sdk_drs.types.participating_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> ParticipatingResources:
    import aws_sdk_drs.types.participating_resource
    out: ParticipatingResources = []
    for item in data:
        out.append(aws_sdk_drs.types.participating_resource.deserialize_json(item))
    return out