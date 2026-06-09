"""Generated from Smithy shape ``com.amazonaws.kms#EncryptionAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

EncryptionAlgorithmSpec: TypeAlias = Literal[
    "SYMMETRIC_DEFAULT",
    "RSAES_OAEP_SHA_1",
    "RSAES_OAEP_SHA_256",
    "SM2PKE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SYMMETRIC_DEFAULT",
        "RSAES_OAEP_SHA_1",
        "RSAES_OAEP_SHA_256",
        "SM2PKE",
    )
)


def serialize_aws_json_1_1(value: EncryptionAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> EncryptionAlgorithmSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown EncryptionAlgorithmSpec value: {data!r}")
    return cast(EncryptionAlgorithmSpec, data)
