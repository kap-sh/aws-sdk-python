"""Generated from Smithy shape ``com.amazonaws.sqs#Binary``."""

import base64
from typing import TypeAlias

Binary: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Binary) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> Binary:
    return base64.b64decode(data)
