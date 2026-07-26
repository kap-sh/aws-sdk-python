"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityDescriptions``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iotthingsgraph.types.entity_description

EntityDescriptions: TypeAlias = list[
    "capo_iotthingsgraph.types.entity_description.EntityDescription"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityDescriptions) -> list:
    import capo_iotthingsgraph.types.entity_description

    out: list = []
    for item in value:
        out.append(
            capo_iotthingsgraph.types.entity_description.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> EntityDescriptions:
    import capo_iotthingsgraph.types.entity_description

    out: EntityDescriptions = []
    for item in data:
        out.append(
            capo_iotthingsgraph.types.entity_description.deserialize_aws_json_1_1(item)
        )
    return out
