"""Generated from Smithy shape ``com.amazonaws.kms#PublicKeyType``."""

import base64
from typing import TypeAlias

PublicKeyType: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PublicKeyType) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> PublicKeyType:
    return base64.b64decode(data)
