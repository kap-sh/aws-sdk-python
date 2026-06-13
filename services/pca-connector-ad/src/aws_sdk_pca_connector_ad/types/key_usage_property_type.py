"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeyUsagePropertyType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pca_connector_ad.errors import DeserializationError

KeyUsagePropertyType: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("ALL",))


def serialize_json(value: KeyUsagePropertyType) -> str:
    return value


def deserialize_json(data: str) -> KeyUsagePropertyType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown KeyUsagePropertyType value: {data!r}")
    return cast(KeyUsagePropertyType, data)
