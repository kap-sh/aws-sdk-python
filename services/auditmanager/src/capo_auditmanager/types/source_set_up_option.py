"""Generated from Smithy shape ``com.amazonaws.auditmanager#SourceSetUpOption``."""

from typing import Literal, TypeAlias, cast

SourceSetUpOption: TypeAlias = Literal[
    "System_Controls_Mapping",
    "Procedural_Controls_Mapping",
]


# --- restJson1 ser/de ---
def serialize_json(value: SourceSetUpOption) -> str:
    return value


def deserialize_json(data: str) -> SourceSetUpOption:
    return cast(SourceSetUpOption, data)
