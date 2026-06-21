"""Generated from Smithy shape ``com.amazonaws.iotthingsgraph#EntityFilterName``."""

from typing import Literal, TypeAlias, cast

EntityFilterName: TypeAlias = Literal[
    "NAME",
    "NAMESPACE",
    "SEMANTIC_TYPE_PATH",
    "REFERENCED_ENTITY_ID",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityFilterName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityFilterName:
    return cast(EntityFilterName, data)
