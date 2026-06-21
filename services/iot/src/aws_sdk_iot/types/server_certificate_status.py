"""Generated from Smithy shape ``com.amazonaws.iot#ServerCertificateStatus``."""

from typing import Literal, TypeAlias, cast

ServerCertificateStatus: TypeAlias = Literal[
    "INVALID",
    "VALID",
]


# --- restJson1 ser/de ---
def serialize_json(value: ServerCertificateStatus) -> str:
    return value


def deserialize_json(data: str) -> ServerCertificateStatus:
    return cast(ServerCertificateStatus, data)
