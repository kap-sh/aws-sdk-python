"""Generated from Smithy shape ``com.amazonaws.costexplorer#AccountScope``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_cost_explorer.errors import DeserializationError

AccountScope: TypeAlias = Literal[
    "PAYER",
    "LINKED",
]


# --- awsJson1_1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "PAYER",
        "LINKED",
    )
)


def serialize_aws_json_1_1(value: AccountScope) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> AccountScope:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountScope value: {data!r}")
    return cast(AccountScope, data)
