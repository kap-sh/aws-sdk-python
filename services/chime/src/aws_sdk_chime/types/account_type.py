"""Generated from Smithy shape ``com.amazonaws.chime#AccountType``."""

from typing import Literal, TypeAlias, cast

AccountType: TypeAlias = Literal[
    "Team",
    "EnterpriseDirectory",
    "EnterpriseLWA",
    "EnterpriseOIDC",
]


# --- restJson1 ser/de ---
def serialize_json(value: AccountType) -> str:
    return value


def deserialize_json(data: str) -> AccountType:
    return cast(AccountType, data)
