"""Generated from Smithy shape ``com.amazonaws.datasync#KerberosKrb5ConfFile``."""

import base64
from typing import TypeAlias

KerberosKrb5ConfFile: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KerberosKrb5ConfFile) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> KerberosKrb5ConfFile:
    return base64.b64decode(data)
