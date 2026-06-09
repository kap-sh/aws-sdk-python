"""Generated from Smithy shape ``com.amazonaws.kms#SigningAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

SigningAlgorithmSpec: TypeAlias = Literal[
    "RSASSA_PSS_SHA_256",
    "RSASSA_PSS_SHA_384",
    "RSASSA_PSS_SHA_512",
    "RSASSA_PKCS1_V1_5_SHA_256",
    "RSASSA_PKCS1_V1_5_SHA_384",
    "RSASSA_PKCS1_V1_5_SHA_512",
    "ECDSA_SHA_256",
    "ECDSA_SHA_384",
    "ECDSA_SHA_512",
    "SM2DSA",
    "ML_DSA_SHAKE_256",
    "ED25519_SHA_512",
    "ED25519_PH_SHA_512",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSASSA_PSS_SHA_256",
        "RSASSA_PSS_SHA_384",
        "RSASSA_PSS_SHA_512",
        "RSASSA_PKCS1_V1_5_SHA_256",
        "RSASSA_PKCS1_V1_5_SHA_384",
        "RSASSA_PKCS1_V1_5_SHA_512",
        "ECDSA_SHA_256",
        "ECDSA_SHA_384",
        "ECDSA_SHA_512",
        "SM2DSA",
        "ML_DSA_SHAKE_256",
        "ED25519_SHA_512",
        "ED25519_PH_SHA_512",
    )
)


def serialize_aws_json_1_1(value: SigningAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningAlgorithmSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningAlgorithmSpec value: {data!r}")
    return cast(SigningAlgorithmSpec, data)
