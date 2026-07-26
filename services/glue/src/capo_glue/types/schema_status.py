"""Generated from Smithy shape ``com.amazonaws.glue#SchemaStatus``."""

from typing import Literal, TypeAlias, cast

SchemaStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaStatus:
    return cast(SchemaStatus, data)
