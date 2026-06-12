"""Generated from Smithy shape ``com.amazonaws.waf#ByteMatchTargetString``."""

import base64
from typing import TypeAlias

ByteMatchTargetString: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ByteMatchTargetString) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ByteMatchTargetString:
    return base64.b64decode(data)
