"""Generated from Smithy shape ``com.amazonaws.iot#CertificateMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CertificateMode: TypeAlias = Literal[
    "DEFAULT",
    "SNI_ONLY",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "DEFAULT",
        "SNI_ONLY",
    )
)


def serialize_json(value: CertificateMode) -> str:
    return value


def deserialize_json(data: str) -> CertificateMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateMode value: {data!r}")
    return cast(CertificateMode, data)
