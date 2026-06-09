"""Generated from Smithy shape ``com.amazonaws.kms#WrappingKeySpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_kms.errors import DeserializationError

WrappingKeySpec: TypeAlias = Literal[
    "RSA_2048",
    "RSA_3072",
    "RSA_4096",
    "SM2",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSA_2048",
        "RSA_3072",
        "RSA_4096",
        "SM2",
    )
)


def serialize_aws_json_1_1(value: WrappingKeySpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> WrappingKeySpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown WrappingKeySpec value: {data!r}")
    return cast(WrappingKeySpec, data)
