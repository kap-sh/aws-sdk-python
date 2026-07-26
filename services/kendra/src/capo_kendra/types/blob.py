"""Generated from Smithy shape ``com.amazonaws.kendra#Blob``."""

import base64
from typing import TypeAlias

Blob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Blob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> Blob:
    return base64.b64decode(data)
