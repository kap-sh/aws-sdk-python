"""Generated from Smithy shape ``com.amazonaws.quicksight#IdentityStore``."""

from typing import Literal, TypeAlias, cast

IdentityStore: TypeAlias = Literal["QUICKSIGHT",]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityStore) -> str:
    return value


def deserialize_json(data: str) -> IdentityStore:
    return cast(IdentityStore, data)
