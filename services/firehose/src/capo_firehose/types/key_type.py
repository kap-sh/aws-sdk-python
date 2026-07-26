"""Generated from Smithy shape ``com.amazonaws.firehose#KeyType``."""

from typing import Literal, TypeAlias, cast

KeyType: TypeAlias = Literal[
    "AWS_OWNED_CMK",
    "CUSTOMER_MANAGED_CMK",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyType:
    return cast(KeyType, data)
