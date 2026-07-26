"""Generated from Smithy shape ``com.amazonaws.emrcontainers#CertificateProviderType``."""

from typing import Literal, TypeAlias, cast

CertificateProviderType: TypeAlias = Literal["PEM",]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateProviderType) -> str:
    return value


def deserialize_json(data: str) -> CertificateProviderType:
    return cast(CertificateProviderType, data)
