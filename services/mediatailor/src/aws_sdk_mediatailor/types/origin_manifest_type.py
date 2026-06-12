"""Generated from Smithy shape ``com.amazonaws.mediatailor#OriginManifestType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_mediatailor.errors import DeserializationError

OriginManifestType: TypeAlias = Literal[
    "SINGLE_PERIOD",
    "MULTI_PERIOD",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "SINGLE_PERIOD",
        "MULTI_PERIOD",
    )
)


def serialize_json(value: OriginManifestType) -> str:
    return value


def deserialize_json(data: str) -> OriginManifestType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown OriginManifestType value: {data!r}")
    return cast(OriginManifestType, data)
