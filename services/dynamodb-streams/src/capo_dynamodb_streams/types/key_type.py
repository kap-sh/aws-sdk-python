"""Generated from Smithy shape ``com.amazonaws.dynamodbstreams#KeyType``."""

from typing import Literal, TypeAlias, cast

KeyType: TypeAlias = Literal[
    "HASH",
    "RANGE",
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: KeyType) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> KeyType:
    return cast(KeyType, data)
