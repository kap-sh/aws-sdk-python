"""Generated from Smithy shape ``com.amazonaws.codecommit#blob``."""

import base64
from typing import TypeAlias

blob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: blob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> blob:
    return base64.b64decode(data)
