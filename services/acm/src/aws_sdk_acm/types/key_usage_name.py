"""Generated from Smithy shape ``com.amazonaws.acm#KeyUsageName``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm.errors import DeserializationError

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
_VALUES: frozenset[str] = frozenset(
    (
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
    )
)


def serialize_aws_json_1_1(value: KeyUsageName) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyUsageName:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyUsageName value: {data!r}")
    return cast(KeyUsageName, data)
