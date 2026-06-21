"""Generated from Smithy shape ``com.amazonaws.workmail#EntityState``."""

from typing import Literal, TypeAlias, cast

EntityState: TypeAlias = Literal[
    "ENABLED",
    "DISABLED",
    "DELETED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: EntityState) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EntityState:
    return cast(EntityState, data)
