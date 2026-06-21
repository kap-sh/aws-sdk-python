"""Generated from Smithy shape ``com.amazonaws.odb#PatchingModeType``."""

from typing import Literal, TypeAlias, cast

PatchingModeType: TypeAlias = Literal[
    "ROLLING",
    "NONROLLING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PatchingModeType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> PatchingModeType:
    return cast(PatchingModeType, data)
