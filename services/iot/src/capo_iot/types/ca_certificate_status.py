"""Generated from Smithy shape ``com.amazonaws.iot#CACertificateStatus``."""

from typing import Literal, TypeAlias, cast

CACertificateStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
]


# --- restJson1 ser/de ---
def serialize_json(value: CACertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> CACertificateStatus:
    return cast(CACertificateStatus, data)
