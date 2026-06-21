"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#EncryptionStatus``."""

from typing import Literal, TypeAlias, cast

EncryptionStatus: TypeAlias = Literal[
    "PENDING",
    "SUCCESS",
    "FAILURE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EncryptionStatus) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> EncryptionStatus:
    return cast(EncryptionStatus, data)
