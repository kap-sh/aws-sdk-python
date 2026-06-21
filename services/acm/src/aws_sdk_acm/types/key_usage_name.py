"""Generated from Smithy shape ``com.amazonaws.acm#KeyUsageName``."""

from typing import Literal, TypeAlias, cast

KeyUsageName: TypeAlias = Literal[
    "DIGITAL_SIGNATURE",
    "NON_REPUDIATION",
    "KEY_ENCIPHERMENT",
    "DATA_ENCIPHERMENT",
    "KEY_AGREEMENT",
    "CERTIFICATE_SIGNING",
    "CRL_SIGNING",
    "ENCIPHER_ONLY",
    "DECIPHER_ONLY",
    "ANY",
    "CUSTOM",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyUsageName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyUsageName:
    return cast(KeyUsageName, data)
