"""Generated from Smithy shape ``com.amazonaws.rekognition#LivenessImageBlob``."""

import base64
from typing import TypeAlias

LivenessImageBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LivenessImageBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> LivenessImageBlob:
    return base64.b64decode(data)
