"""Generated from Smithy shape ``com.amazonaws.glue#CustomEntityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_glue.types.custom_entity_type

CustomEntityTypes: TypeAlias = list[
    "capo_glue.types.custom_entity_type.CustomEntityType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomEntityTypes) -> list:
    import capo_glue.types.custom_entity_type

    out: list = []
    for item in value:
        out.append(capo_glue.types.custom_entity_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomEntityTypes:
    import capo_glue.types.custom_entity_type

    out: CustomEntityTypes = []
    for item in data:
        out.append(capo_glue.types.custom_entity_type.deserialize_aws_json_1_1(item))
    return out
