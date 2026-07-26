"""Generated from Smithy shape ``com.amazonaws.glue#Permission``."""

from typing import Literal, TypeAlias, cast

Permission: TypeAlias = Literal[
    "ALL",
    "SELECT",
    "ALTER",
    "DROP",
    "DELETE",
    "INSERT",
    "CREATE_DATABASE",
    "CREATE_TABLE",
    "DATA_LOCATION_ACCESS",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Permission) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> Permission:
    return cast(Permission, data)
