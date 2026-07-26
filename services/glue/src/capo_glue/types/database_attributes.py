"""Generated from Smithy shape ``com.amazonaws.glue#DatabaseAttributes``."""

from typing import Literal, TypeAlias, cast

DatabaseAttributes: TypeAlias = Literal[
    "NAME",
    "TARGET_DATABASE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DatabaseAttributes) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DatabaseAttributes:
    return cast(DatabaseAttributes, data)
