"""Generated from Smithy shape ``com.amazonaws.appintegrations#ContactHandlingScope``."""

from typing import Literal, TypeAlias, cast

ContactHandlingScope: TypeAlias = Literal[
    "CROSS_CONTACTS",
    "PER_CONTACT",
]


# --- restJson1 ser/de ---
def serialize_json(value: ContactHandlingScope) -> str:
    return value


def deserialize_json(data: str) -> ContactHandlingScope:
    return cast(ContactHandlingScope, data)
