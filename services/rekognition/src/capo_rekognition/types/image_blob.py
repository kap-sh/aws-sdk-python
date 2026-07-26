"""Generated from Smithy shape ``com.amazonaws.rekognition#ImageBlob``."""

import base64
from typing import TypeAlias

ImageBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImageBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ImageBlob:
    return base64.b64decode(data)
