"""Generated from Smithy shape ``com.amazonaws.dynamodb#BinaryAttributeValue``."""

from typing import TypeAlias
import base64

BinaryAttributeValue: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: BinaryAttributeValue) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> BinaryAttributeValue:
    return base64.b64decode(data)
