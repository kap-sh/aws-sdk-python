"""Generated from Smithy shape ``com.amazonaws.kms#MacAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast
from aws_sdk_kms.errors import DeserializationError

MacAlgorithmSpec: TypeAlias = Literal[
    "HMAC_SHA_224",
    "HMAC_SHA_256",
    "HMAC_SHA_384",
    "HMAC_SHA_512",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "HMAC_SHA_224",
        "HMAC_SHA_256",
        "HMAC_SHA_384",
        "HMAC_SHA_512",
    )
)


def serialize_aws_json_1_1(value: MacAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MacAlgorithmSpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown MacAlgorithmSpec value: {data!r}")
    return cast(MacAlgorithmSpec, data)
