"""Generated from Smithy shape ``com.amazonaws.kms#AlgorithmSpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

AlgorithmSpec: TypeAlias = Literal[
    "RSAES_PKCS1_V1_5",
    "RSAES_OAEP_SHA_1",
    "RSAES_OAEP_SHA_256",
    "RSA_AES_KEY_WRAP_SHA_1",
    "RSA_AES_KEY_WRAP_SHA_256",
    "SM2PKE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSAES_PKCS1_V1_5",
        "RSAES_OAEP_SHA_1",
        "RSAES_OAEP_SHA_256",
        "RSA_AES_KEY_WRAP_SHA_1",
        "RSA_AES_KEY_WRAP_SHA_256",
        "SM2PKE",
    )
)


def serialize_aws_json_1_1(value: AlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AlgorithmSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AlgorithmSpec value: {data!r}")
    return cast(AlgorithmSpec, data)
