"""Generated from Smithy shape ``com.amazonaws.datasync#ObjectStorageCertificate``."""

import base64
from typing import TypeAlias

ObjectStorageCertificate: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ObjectStorageCertificate) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> ObjectStorageCertificate:
    return base64.b64decode(data)
