"""Generated from Smithy shape ``com.amazonaws.acm#KeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

KeyAlgorithm: TypeAlias = Literal[
    "RSA_1024",
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "EC_prime256v1",
    "EC_secp384r1",
    "EC_secp521r1",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: KeyAlgorithm) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> KeyAlgorithm:
    return cast(KeyAlgorithm, data)
