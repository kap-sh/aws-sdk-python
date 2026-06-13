"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#PrivateKeyAlgorithm``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

PrivateKeyAlgorithm: TypeAlias = Literal[
    "RSA",
    "ECDH_P256",
    "ECDH_P384",
    "ECDH_P521",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "RSA",
        "ECDH_P256",
        "ECDH_P384",
        "ECDH_P521",
    )
)


def serialize_json(value: PrivateKeyAlgorithm) -> str:
    return value


def deserialize_json(data: str) -> PrivateKeyAlgorithm:
    if data not in _VALUES:
        raise DeserializationError(f"unknown PrivateKeyAlgorithm value: {data!r}")
    return cast(PrivateKeyAlgorithm, data)
