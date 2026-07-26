"""Generated from Smithy shape ``com.amazonaws.kms#KeyManagerType``."""

from typing import Literal, TypeAlias, cast

KeyManagerType: TypeAlias = Literal[
    "AWS",
    "CUSTOMER",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyManagerType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyManagerType:
    return cast(KeyManagerType, data)
