"""Generated from Smithy shape ``com.amazonaws.iot#CertificateProviderOperation``."""

from typing import Literal, TypeAlias, cast

CertificateProviderOperation: TypeAlias = Literal["CreateCertificateFromCsr",]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateProviderOperation) -> str:
    return value


def deserialize_json(data: str) -> CertificateProviderOperation:
    return cast(CertificateProviderOperation, data)
