"""Generated from Smithy shape ``com.amazonaws.glue#SchemaVersionStatus``."""

from typing import Literal, TypeAlias, cast

SchemaVersionStatus: TypeAlias = Literal[
    "AVAILABLE",
    "PENDING",
    "FAILURE",
    "DELETING",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SchemaVersionStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SchemaVersionStatus:
    return cast(SchemaVersionStatus, data)
