"""Generated from Smithy shape ``com.amazonaws.kms#CustomerMasterKeySpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

CustomerMasterKeySpec: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "ECC_NIST_P256",
    "ECC_NIST_P384",
    "ECC_NIST_P521",
    "ECC_SECG_P256K1",
    "SYMMETRIC_DEFAULT",
    "HMAC_224",
    "HMAC_256",
    "HMAC_384",
    "HMAC_512",
    "SM2",
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
        "SYMMETRIC_DEFAULT",
        "HMAC_224",
        "HMAC_256",
        "HMAC_384",
        "HMAC_512",
        "SM2",
    )
)


def serialize_aws_json_1_1(value: CustomerMasterKeySpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CustomerMasterKeySpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CustomerMasterKeySpec value: {data!r}")
    return cast(CustomerMasterKeySpec, data)
