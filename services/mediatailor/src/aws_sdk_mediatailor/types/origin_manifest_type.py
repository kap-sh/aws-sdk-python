"""Generated from Smithy shape ``com.amazonaws.mediatailor#OriginManifestType``."""

from typing import Literal, TypeAlias, cast

OriginManifestType: TypeAlias = Literal[
    "SINGLE_PERIOD",
    "MULTI_PERIOD",
]


# --- restJson1 ser/de ---
def serialize_json(value: OriginManifestType) -> str:
    return value


def deserialize_json(data: str) -> OriginManifestType:
    return cast(OriginManifestType, data)
