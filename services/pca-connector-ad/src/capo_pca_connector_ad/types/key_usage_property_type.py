"""Generated from Smithy shape ``com.amazonaws.pcaconnectorad#KeyUsagePropertyType``."""

from typing import Literal, TypeAlias, cast

KeyUsagePropertyType: TypeAlias = Literal["ALL",]


# --- restJson1 ser/de ---
def serialize_json(value: KeyUsagePropertyType) -> str:
    return value


def deserialize_json(data: str) -> KeyUsagePropertyType:
    return cast(KeyUsagePropertyType, data)
