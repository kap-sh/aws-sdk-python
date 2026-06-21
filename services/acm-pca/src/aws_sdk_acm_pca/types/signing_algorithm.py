"""Generated from Smithy shape ``com.amazonaws.acmpca#SigningAlgorithm``."""

from typing import Literal, TypeAlias, cast

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
def serialize_aws_json_1_1(value: SigningAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningAlgorithm:
    return cast(SigningAlgorithm, data)
