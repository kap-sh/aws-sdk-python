"""Generated from Smithy shape ``com.amazonaws.signer#HashAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_signer.errors import DeserializationError

HashAlgorithm: TypeAlias = Literal[
    "SHA1",
    "SHA256",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA1",
        "SHA256",
    )
)


def serialize_json(value: HashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> HashAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HashAlgorithm value: {data!r}")
    return cast(HashAlgorithm, data)
