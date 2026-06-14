"""Generated from Smithy shape ``com.amazonaws.workspaces#Ios3XLogo``."""

import base64
from typing import TypeAlias

Ios3XLogo: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ios3XLogo) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> Ios3XLogo:
    return base64.b64decode(data)
