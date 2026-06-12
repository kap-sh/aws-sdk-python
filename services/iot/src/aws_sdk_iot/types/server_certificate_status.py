"""Generated from Smithy shape ``com.amazonaws.iot#ServerCertificateStatus``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

ServerCertificateStatus: TypeAlias = Literal[
    "INVALID",
    "VALID",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "INVALID",
        "VALID",
    )
)


def serialize_json(value: ServerCertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> ServerCertificateStatus:
    if data not in _VALUES:
        raise DeserializationError(f"unknown ServerCertificateStatus value: {data!r}")
    return cast(ServerCertificateStatus, data)
