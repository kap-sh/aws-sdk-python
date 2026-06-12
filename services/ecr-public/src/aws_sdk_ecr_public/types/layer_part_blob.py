"""Generated from Smithy shape ``com.amazonaws.ecrpublic#LayerPartBlob``."""

import base64
from typing import TypeAlias

LayerPartBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LayerPartBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> LayerPartBlob:
    return base64.b64decode(data)
