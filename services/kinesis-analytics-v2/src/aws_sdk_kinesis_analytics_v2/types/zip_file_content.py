"""Generated from Smithy shape ``com.amazonaws.kinesisanalyticsv2#ZipFileContent``."""

import base64
from typing import TypeAlias

ZipFileContent: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ZipFileContent) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ZipFileContent:
    return base64.b64decode(data)
