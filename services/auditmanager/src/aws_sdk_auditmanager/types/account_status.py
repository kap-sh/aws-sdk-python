"""Generated from Smithy shape ``com.amazonaws.auditmanager#AccountStatus``."""

from typing import Literal, TypeAlias, cast

AccountStatus: TypeAlias = Literal[
    "ACTIVE",
    "INACTIVE",
    "PENDING_ACTIVATION",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountStatus) -> str:
    return value


def deserialize_json(data: str) -> AccountStatus:
    return cast(AccountStatus, data)
