"""Generated from Smithy shape ``com.amazonaws.sfn#KmsKeyState``."""

from typing import Literal, TypeAlias, cast

KmsKeyState: TypeAlias = Literal[
    "DISABLED",
    "PENDING_DELETION",
    "PENDING_IMPORT",
    "UNAVAILABLE",
    "CREATING",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KmsKeyState) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KmsKeyState:
    return cast(KmsKeyState, data)
