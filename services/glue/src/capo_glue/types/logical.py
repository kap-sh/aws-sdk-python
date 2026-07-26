"""Generated from Smithy shape ``com.amazonaws.glue#Logical``."""

from typing import Literal, TypeAlias, cast

Logical: TypeAlias = Literal[
    "AND",
    "ANY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Logical) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Logical:
    return cast(Logical, data)
