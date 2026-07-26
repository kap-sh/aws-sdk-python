"""Generated from Smithy shape ``com.amazonaws.iot#RelatedResources``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.related_resource

RelatedResources: TypeAlias = list["capo_iot.types.related_resource.RelatedResource"]


# --- restJson1 ser/de ---
def serialize_json(value: RelatedResources) -> list:
    import capo_iot.types.related_resource

    out: list = []
    for item in value:
        out.append(capo_iot.types.related_resource.serialize_json(item))
    return out


def deserialize_json(data: list) -> RelatedResources:
    import capo_iot.types.related_resource

    out: RelatedResources = []
    for item in data:
        out.append(capo_iot.types.related_resource.deserialize_json(item))
    return out
