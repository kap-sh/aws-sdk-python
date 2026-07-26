"""Generated from Smithy shape ``com.amazonaws.amplify#CertificateType``."""

from typing import Literal, TypeAlias, cast

CertificateType: TypeAlias = Literal[
    "AMPLIFY_MANAGED",
    "CUSTOM",
]


# --- restJson1 ser/de ---
def serialize_json(value: CertificateType) -> str:
    return value


def deserialize_json(data: str) -> CertificateType:
    return cast(CertificateType, data)
