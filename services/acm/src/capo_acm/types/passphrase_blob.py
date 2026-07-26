"""Generated from Smithy shape ``com.amazonaws.acm#PassphraseBlob``."""

import base64
from typing import TypeAlias

PassphraseBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PassphraseBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> PassphraseBlob:
    return base64.b64decode(data)
