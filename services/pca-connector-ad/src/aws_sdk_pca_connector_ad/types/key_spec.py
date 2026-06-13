"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeySpec``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

KeySpec: TypeAlias = Literal[
    "KEY_EXCHANGE",
    "SIGNATURE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "KEY_EXCHANGE",
        "SIGNATURE",
    )
)


def serialize_json(value: KeySpec) -> str:
    return value


def deserialize_json(data: str) -> KeySpec:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeySpec value: {data!r}")
    return cast(KeySpec, data)
