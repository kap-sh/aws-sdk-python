"""Generated from Smithy shape ``com.amazonaws.iot#CertificateMode``."""

from typing import Literal, TypeAlias, cast

CertificateMode: TypeAlias = Literal[
    "DEFAULT",
    "SNI_ONLY",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateMode) -> str:
    return value


def deserialize_json(data: str) -> CertificateMode:
    return cast(CertificateMode, data)
