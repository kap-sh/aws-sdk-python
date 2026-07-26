"""Generated from Smithy shape ``com.amazonaws.cognitoidentityprovider#AssetBytesType``."""

import base64
from typing import TypeAlias

AssetBytesType: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssetBytesType) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> AssetBytesType:
    return base64.b64decode(data)
