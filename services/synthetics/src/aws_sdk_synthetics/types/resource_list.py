"""Generated from Smithy shape ``com.amazonaws.synthetics#ResourceList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_synthetics.types.resource_to_tag

ResourceList: TypeAlias = list["aws_sdk_synthetics.types.resource_to_tag.ResourceToTag"]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceList) -> list:
    import aws_sdk_synthetics.types.resource_to_tag

    out: list = []
    for item in value:
        out.append(aws_sdk_synthetics.types.resource_to_tag.serialize_json(item))
    return out


def deserialize_json(data: list) -> ResourceList:
    import aws_sdk_synthetics.types.resource_to_tag

    out: ResourceList = []
    for item in data:
        out.append(aws_sdk_synthetics.types.resource_to_tag.deserialize_json(item))
    return out
