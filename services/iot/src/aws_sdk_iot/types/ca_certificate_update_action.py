"""Generated from Smithy shape ``com.amazonaws.iot#CACertificateUpdateAction``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CACertificateUpdateAction: TypeAlias = Literal["DEACTIVATE",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("DEACTIVATE",))


def serialize_json(value: CACertificateUpdateAction) -> str:
    return value


def deserialize_json(data: str) -> CACertificateUpdateAction:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CACertificateUpdateAction value: {data!r}")
    return cast(CACertificateUpdateAction, data)
