"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#KeyType``."""

from typing import Literal, TypeAlias, cast

KeyType: TypeAlias = Literal[
    "AWS_OWNED_KEY",
    "CUSTOMER_MANAGED_KEY",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyType:
    return cast(KeyType, data)
