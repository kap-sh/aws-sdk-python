"""Generated from Smithy shape ``com.amazonaws.kms#DataKeyPairSpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

DataKeyPairSpec: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "SM2",
    "ECC_NIST_EDWARDS25519",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "ECC_NIST_P256",
        "ECC_NIST_P384",
        "ECC_NIST_P521",
        "ECC_SECG_P256K1",
        "SM2",
        "ECC_NIST_EDWARDS25519",
    )
)


def serialize_aws_json_1_1(value: DataKeyPairSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> DataKeyPairSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DataKeyPairSpec value: {data!r}")
    return cast(DataKeyPairSpec, data)
