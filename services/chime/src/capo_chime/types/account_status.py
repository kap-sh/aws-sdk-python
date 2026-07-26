"""Generated from Smithy shape ``com.amazonaws.chime#AccountStatus``."""

from typing import Literal, TypeAlias, cast

AccountStatus: TypeAlias = Literal[
    "Suspended",
    "Active",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AccountStatus:
    return cast(AccountStatus, data)
