"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#HashAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

HashAlgorithm: TypeAlias = Literal[
    "SHA256",
    "SHA384",
    "SHA512",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SHA256",
        "SHA384",
        "SHA512",
    )
)


def serialize_json(value: HashAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> HashAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown HashAlgorithm value: {data!r}")
    return cast(HashAlgorithm, data)
