"""Generated from Smithy shape ``com.amazonaws.databasemigrationservice#CertificateWallet``."""

import base64
from typing import TypeAlias

CertificateWallet: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CertificateWallet) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> CertificateWallet:
    return base64.b64decode(data)
