"""Generated from Smithy shape ``com.amazonaws.acmpca#KeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

KeyAlgorithm: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "EC_prime256v1",
    "EC_secp384r1",
    "EC_secp521r1",
    "ML_DSA_44",
    "ML_DSA_65",
    "ML_DSA_87",
    "SM2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "EC_prime256v1",
        "EC_secp384r1",
        "EC_secp521r1",
        "ML_DSA_44",
        "ML_DSA_65",
        "ML_DSA_87",
        "SM2",
    )
)


def serialize_aws_json_1_1(value: KeyAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyAlgorithm value: {data!r}")
    return cast(KeyAlgorithm, data)
