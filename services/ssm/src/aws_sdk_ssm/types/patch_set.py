"""Generated from Smithy shape ``com.amazonaws.ssm#PatchSet``."""

from typing import Literal, TypeAlias, cast

PatchSet: TypeAlias = Literal[
    "OS",
    "APPLICATION",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchSet) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchSet:
    return cast(PatchSet, data)
