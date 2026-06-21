"""Generated from Smithy shape ``com.amazonaws.datasync#OverwriteMode``."""

from typing import Literal, TypeAlias, cast

OverwriteMode: TypeAlias = Literal[
    "ALWAYS",
    "NEVER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: OverwriteMode) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> OverwriteMode:
    return cast(OverwriteMode, data)
