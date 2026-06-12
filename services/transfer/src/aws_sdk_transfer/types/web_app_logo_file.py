"""Generated from Smithy shape ``com.amazonaws.transfer#WebAppLogoFile``."""

import base64
from typing import TypeAlias

WebAppLogoFile: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WebAppLogoFile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> WebAppLogoFile:
    return base64.b64decode(data)
