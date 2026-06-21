"""Generated from Smithy shape ``com.amazonaws.kms#WrappingKeySpec``."""

from typing import Literal, TypeAlias, cast

WrappingKeySpec: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "SM2",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: WrappingKeySpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WrappingKeySpec:
    return cast(WrappingKeySpec, data)
