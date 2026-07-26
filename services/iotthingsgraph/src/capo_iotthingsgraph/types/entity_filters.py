"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityFilters``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.entity_filter

EntityFilters: TypeAlias = list["capo_iotthingsgraph.types.entity_filter.EntityFilter"]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilters) -> list:
    import capo_iotthingsgraph.types.entity_filter

    out: list = []
    for item in value:
        out.append(capo_iotthingsgraph.types.entity_filter.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> EntityFilters:
    import capo_iotthingsgraph.types.entity_filter

    out: EntityFilters = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.entity_filter.deserialize_aws_json_1_1(item)
        )
    return out
