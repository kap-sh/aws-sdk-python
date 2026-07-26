"""Generated from Smithy shape ``com.amazonaws.connecthealth#DomainStatus``."""

from typing import Literal, TypeAlias, cast

DomainStatus: TypeAlias = Literal[
    "ACTIVE",
    "DELETING",
    "DELETED",
]


# --- restJson1 ser/de ---
def serialize_json(value: DomainStatus) -> str:
    return value


def deserialize_json(data: str) -> DomainStatus:
    return cast(DomainStatus, data)
