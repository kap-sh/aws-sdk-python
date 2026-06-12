"""Generated from Smithy shape ``com.amazonaws.cloudtrail#ByteBuffer``."""

import base64
from typing import TypeAlias

ByteBuffer: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteBuffer) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ByteBuffer:
    return base64.b64decode(data)
