"""Generated from Smithy shape ``com.amazonaws.iot#CertificateProviderOperation``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_iot.errors import DeserializationError

CertificateProviderOperation: TypeAlias = Literal["CreateCertificateFromCsr",]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(("CreateCertificateFromCsr",))


def serialize_json(value: CertificateProviderOperation) -> str:
    return value


def deserialize_json(data: str) -> CertificateProviderOperation:
    if data not in _VALUES:
        raise DeserializationError(
            f"unknown CertificateProviderOperation value: {data!r}"
        )
    return cast(CertificateProviderOperation, data)
