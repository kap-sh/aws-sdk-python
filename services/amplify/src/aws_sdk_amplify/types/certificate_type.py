"""Generated from Smithy shape ``com.amazonaws.amplify#CertificateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_amplify.errors import DeserializationError

CertificateType: TypeAlias = Literal[
    "AMPLIFY_MANAGED",
    "CUSTOM",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "AMPLIFY_MANAGED",
        "CUSTOM",
    )
)


def serialize_json(value: CertificateType) -> str:
    return value


def deserialize_json(data: str) -> CertificateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateType value: {data!r}")
    return cast(CertificateType, data)
