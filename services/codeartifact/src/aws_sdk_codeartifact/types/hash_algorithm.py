"""Generated from Smithy shape ``com.amazonaws.codeartifact#HashAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_codeartifact.errors import DeserializationError

HashAlgorithm: TypeAlias = Literal[
    "MD5",
    "SHA-1",
    "SHA-256",
    "SHA-512",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "MD5",
        "SHA-1",
        "SHA-256",
        "SHA-512",
    )
)


def serialize_json(value: HashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> HashAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HashAlgorithm value: {data!r}")
    return cast(HashAlgorithm, data)
