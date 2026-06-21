"""Generated from Smithy shape ``com.amazonaws.iot#CACertificateUpdateAction``."""

from typing import Literal, TypeAlias, cast

CACertificateUpdateAction: TypeAlias = Literal["DEACTIVATE",]


# --- restJson1 ser/de ---
def serialize_json(value: CACertificateUpdateAction) -> str:
    return value


def deserialize_json(data: str) -> CACertificateUpdateAction:
    return cast(CACertificateUpdateAction, data)
