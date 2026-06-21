"""Generated from Smithy shape ``com.amazonaws.directoryservicedata#GroupScope``."""

from typing import Literal, TypeAlias, cast

GroupScope: TypeAlias = Literal[
    "DomainLocal",
    "Global",
    "Universal",
    "BuiltinLocal",
]


# --- restJson1 ser/de ---
def serialize_json(value: GroupScope) -> str:
    return value


def deserialize_json(data: str) -> GroupScope:
    return cast(GroupScope, data)
