"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#ImageFileType``."""

import base64
from typing import TypeAlias

ImageFileType: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageFileType) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ImageFileType:
    return base64.b64decode(data)
