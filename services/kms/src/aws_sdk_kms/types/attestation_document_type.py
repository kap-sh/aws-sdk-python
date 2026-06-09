"""Generated from Smithy shape ``com.amazonaws.kms#AttestationDocumentType``."""

from typing import TypeAlias
import base64

AttestationDocumentType: TypeAlias = bytes


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttestationDocumentType) -> str:
    return base64.b64encode(value).decode("ascii")


def deserialize_aws_json_1_1(data: str) -> AttestationDocumentType:
    return base64.b64decode(data)
