"""Generated from Smithy shape ``com.amazonaws.wafv2#SearchString``."""

import base64
from typing import TypeAlias

SearchString: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SearchString) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> SearchString:
    return base64.b64decode(data)
