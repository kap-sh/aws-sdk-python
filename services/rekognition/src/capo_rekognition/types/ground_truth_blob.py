"""Generated from Smithy shape ``com.amazonaws.rekognition#GroundTruthBlob``."""

import base64
from typing import TypeAlias

GroundTruthBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GroundTruthBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> GroundTruthBlob:
    return base64.b64decode(data)
