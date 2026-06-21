"""Generated from Smithy shape ``com.amazonaws.ssm#PatchAction``."""

from typing import Literal, TypeAlias, cast

PatchAction: TypeAlias = Literal[
    "ALLOW_AS_DEPENDENCY",
    "BLOCK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchAction) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchAction:
    return cast(PatchAction, data)
