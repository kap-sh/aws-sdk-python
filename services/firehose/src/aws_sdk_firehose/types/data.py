"""Generated from Smithy shape ``com.amazonaws.firehose#Data``."""

import base64
from typing import TypeAlias

Data: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Data) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> Data:
    return base64.b64decode(data)
