"""Generated from Smithy shape ``com.amazonaws.codecommit#FileContent``."""

import base64
from typing import TypeAlias

FileContent: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FileContent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> FileContent:
    return base64.b64decode(data)
