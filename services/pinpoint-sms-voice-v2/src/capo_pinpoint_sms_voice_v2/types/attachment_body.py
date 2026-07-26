"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#AttachmentBody``."""

import base64
from typing import TypeAlias

AttachmentBody: TypeAlias = bytes


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AttachmentBody) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_0(data: str) -> AttachmentBody:
    return base64.b64decode(data)
