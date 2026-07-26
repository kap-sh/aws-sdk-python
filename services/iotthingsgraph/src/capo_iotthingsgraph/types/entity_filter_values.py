"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityFilterValues``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.entity_filter_value

EntityFilterValues: TypeAlias = list[
    "capo_iotthingsgraph.types.entity_filter_value.EntityFilterValue"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilterValues) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> EntityFilterValues:
    return list(data)
