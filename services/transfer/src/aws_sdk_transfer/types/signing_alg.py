"""Generated from Smithy shape ``com.amazonaws.transfer#SigningAlg``."""

from typing import Literal, TypeAlias, cast

SigningAlg: TypeAlias = Literal[
    "SHA256",
    "SHA384",
    "SHA512",
    "SHA1",
    "NONE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SigningAlg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningAlg:
    return cast(SigningAlg, data)
