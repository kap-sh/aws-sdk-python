"""Generated from Smithy shape ``com.amazonaws.ssoadmin#KmsKeyStatus``."""

from typing import Literal, TypeAlias, cast

KmsKeyStatus: TypeAlias = Literal[
    "UPDATING",
    "ENABLED",
    "UPDATE_FAILED",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KmsKeyStatus) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KmsKeyStatus:
    return cast(KmsKeyStatus, data)
