"""Generated from Smithy shape ``com.amazonaws.iot#CACertificateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CACertificateStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACTIVE",
        "INACTIVE",
    )
)


def serialize_json(value: CACertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> CACertificateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CACertificateStatus value: {data!r}")
    return cast(CACertificateStatus, data)
