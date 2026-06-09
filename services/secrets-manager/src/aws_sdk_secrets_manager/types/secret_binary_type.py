"""Generated from Smithy shape ``com.amazonaws.secretsmanager#SecretBinaryType``."""

import base64
from typing import TypeAlias

SecretBinaryType: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SecretBinaryType) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> SecretBinaryType:
    return base64.b64decode(data)
