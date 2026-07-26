"""Generated from Smithy shape ``com.amazonaws.transfer#OverwriteExisting``."""

from typing import Literal, TypeAlias, cast

OverwriteExisting: TypeAlias = Literal[
    "TRUE",
    "FALSE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverwriteExisting) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteExisting:
    return cast(OverwriteExisting, data)
