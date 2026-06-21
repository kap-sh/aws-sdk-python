"""Generated from Smithy shape ``com.amazonaws.kms#MacAlgorithmSpec``."""

from typing import Literal, TypeAlias, cast

MacAlgorithmSpec: TypeAlias = Literal[
    "HMAC_SHA_224",
    "HMAC_SHA_256",
    "HMAC_SHA_384",
    "HMAC_SHA_512",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: MacAlgorithmSpec) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> MacAlgorithmSpec:
    return cast(MacAlgorithmSpec, data)
