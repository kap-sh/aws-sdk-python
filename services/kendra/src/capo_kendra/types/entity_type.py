"""Generated from Smithy shape ``com.amazonaws.kendra#EntityType``."""

from typing import Literal, TypeAlias, cast

EntityType: TypeAlias = Literal[
    "USER",
    "GROUP",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityType:
    return cast(EntityType, data)
