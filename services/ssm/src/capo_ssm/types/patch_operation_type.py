"""Generated from Smithy shape ``com.amazonaws.ssm#PatchOperationType``."""

from typing import Literal, TypeAlias, cast

PatchOperationType: TypeAlias = Literal[
    "Scan",
    "Install",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PatchOperationType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> PatchOperationType:
    return cast(PatchOperationType, data)
