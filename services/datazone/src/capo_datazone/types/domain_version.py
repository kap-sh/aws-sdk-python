"""Generated from Smithy shape ``com.amazonaws.datazone#DomainVersion``."""

from typing import Literal, TypeAlias, cast

DomainVersion: TypeAlias = Literal[
    "V1",
    "V2",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainVersion) -> str:
    return value


def deserialize_json(data: str) -> DomainVersion:
    return cast(DomainVersion, data)
