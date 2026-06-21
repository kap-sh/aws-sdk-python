"""Generated from Smithy shape ``com.amazonaws.odb#CloneType``."""

from typing import Literal, TypeAlias, cast

CloneType: TypeAlias = Literal[
    "FULL",
    "METADATA",
    "PARTIAL",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CloneType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> CloneType:
    return cast(CloneType, data)
