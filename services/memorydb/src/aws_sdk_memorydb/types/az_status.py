"""Generated from Smithy shape ``com.amazonaws.memorydb#AZStatus``."""

from typing import Literal, TypeAlias, cast

AZStatus: TypeAlias = Literal[
    "singleaz",
    "multiaz",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AZStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AZStatus:
    return cast(AZStatus, data)
