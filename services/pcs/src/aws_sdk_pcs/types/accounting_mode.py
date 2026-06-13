"""Generated from Smithy shape ``com.amazonaws.pcs#AccountingMode``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_pcs.errors import DeserializationError

AccountingMode: TypeAlias = Literal[
    "STANDARD",
    "NONE",
]


# --- awsJson1_0 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "STANDARD",
        "NONE",
    )
)


def serialize_aws_json_1_0(value: AccountingMode) -> str:
    return value


def deserialize_aws_json_1_0(data: str) -> AccountingMode:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AccountingMode value: {data!r}")
    return cast(AccountingMode, data)
