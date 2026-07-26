"""Generated from Smithy shape ``com.amazonaws.acm#CertificateChainBlob``."""

import base64
from typing import TypeAlias

CertificateChainBlob: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateChainBlob) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> CertificateChainBlob:
    return base64.b64decode(data)
