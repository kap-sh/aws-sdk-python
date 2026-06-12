"""Generated from Smithy shape ``com.amazonaws.transfer#SigningAlg``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_transfer.errors import DeserializationError

SigningAlg: TypeAlias = Literal[
    "SHA256",
    "SHA384",
    "SHA512",
    "SHA1",
    "NONE",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA256",
        "SHA384",
        "SHA512",
        "SHA1",
        "NONE",
    )
)


def serialize_aws_json_1_1(value: SigningAlg) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> SigningAlg:
    if data not in _VALUES:
        raise DeserializationError(f"unknown SigningAlg value: {data!r}")
    return cast(SigningAlg, data)
