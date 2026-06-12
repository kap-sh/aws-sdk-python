"""Generated from Smithy shape ``com.amazonaws.chime#AccountType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_chime.errors import DeserializationError

AccountType: TypeAlias = Literal[
    "Team",
    "EnterpriseDirectory",
    "EnterpriseLWA",
    "EnterpriseOIDC",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Team",
        "EnterpriseDirectory",
        "EnterpriseLWA",
        "EnterpriseOIDC",
    )
)


def serialize_json(value: AccountType) -> str:
    return value


def deserialize_json(data: str) -> AccountType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountType value: {data!r}")
    return cast(AccountType, data)
