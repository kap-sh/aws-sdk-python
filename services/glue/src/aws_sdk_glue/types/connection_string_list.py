"""Generated from Smithy shape ``com.amazonaws.glue#ConnectionStringList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_glue.types.connection_string

ConnectionStringList: TypeAlias = list[
    "aws_sdk_glue.types.connection_string.ConnectionString"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionStringList) -> list:
    return list(value)


def deserialize_aws_json_1_1(data: list) -> ConnectionStringList:
    return list(data)
