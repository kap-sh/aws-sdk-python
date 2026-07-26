"""Generated from Smithy shape ``com.amazonaws.kms#CiphertextType``."""

import base64
from typing import TypeAlias

CiphertextType: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CiphertextType) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> CiphertextType:
    return base64.b64decode(data)
