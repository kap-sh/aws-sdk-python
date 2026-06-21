"""Generated from Smithy shape ``com.amazonaws.mediapackagev2#CmafEncryptionMethod``."""

from typing import Literal, TypeAlias, cast

CmafEncryptionMethod: TypeAlias = Literal[
    "CENC",
    "CBCS",
]


# --- restJson1 ser/de ---
def serialize_json(value: CmafEncryptionMethod) -> str:
    return value


def deserialize_json(data: str) -> CmafEncryptionMethod:
    return cast(CmafEncryptionMethod, data)
