"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#NetworkFileBlob``."""

import base64
from typing import TypeAlias

NetworkFileBlob: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: NetworkFileBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> NetworkFileBlob:
    return base64.b64decode(data)
