"""Generated from Smithy shape ``com.amazonaws.acmpca#SigningAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_acm_pca.errors import DeserializationError

SigningAlgorithm: TypeAlias = Literal[
    "SHA256WITHECDSA",
    "SHA384WITHECDSA",
    "SHA512WITHECDSA",
    "SHA256WITHRSA",
    "SHA384WITHRSA",
    "SHA512WITHRSA",
    "SM3WITHSM2",
    "ML_DSA_44",
    "ML_DSA_65",
    "ML_DSA_87",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA256WITHECDSA",
        "SHA384WITHECDSA",
        "SHA512WITHECDSA",
        "SHA256WITHRSA",
        "SHA384WITHRSA",
        "SHA512WITHRSA",
        "SM3WITHSM2",
        "ML_DSA_44",
        "ML_DSA_65",
        "ML_DSA_87",
    )
)


def serialize_aws_json_1_1(value: SigningAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningAlgorithm value: {data!r}")
    return cast(SigningAlgorithm, data)
