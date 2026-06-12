"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CertificateProviderType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_emr_containers.errors import DeserializationError

CertificateProviderType: TypeAlias = Literal["PEM",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("PEM",))


def serialize_json(value: CertificateProviderType) -> str:
    return value


def deserialize_json(data: str) -> CertificateProviderType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown CertificateProviderType value: {data!r}")
    return cast(CertificateProviderType, data)
