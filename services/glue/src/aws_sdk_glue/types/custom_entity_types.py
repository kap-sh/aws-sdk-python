"""Generated from Smithy shape ``com.amazonaws.glue#CustomEntityTypes``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.custom_entity_type

CustomEntityTypes: TypeAlias = list[
    "aws_sdk_glue.types.custom_entity_type.CustomEntityType"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CustomEntityTypes) -> list:
    import aws_sdk_glue.types.custom_entity_type

    out: list = []
    for item in value:
        out.append(aws_sdk_glue.types.custom_entity_type.serialize_aws_json_1_1(item))
    return out


def deserialize_aws_json_1_1(data: list) -> CustomEntityTypes:
    import aws_sdk_glue.types.custom_entity_type

    out: CustomEntityTypes = []
    for item in data:
        out.append(aws_sdk_glue.types.custom_entity_type.deserialize_aws_json_1_1(item))
    return out
