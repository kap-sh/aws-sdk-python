"""Generated from Smithy shape ``com.amazonaws.securityhub#AutoEnableStandards``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_securityhub.errors import DeserializationError

AutoEnableStandards: TypeAlias = Literal[
    "NONE",
    "DEFAULT",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "NONE",
        "DEFAULT",
    )
)


def serialize_json(value: AutoEnableStandards) -> str:
    return value


def deserialize_json(data: str) -> AutoEnableStandards:
    if data not in _VALUES:
        raise DeserializationError(f"unknown AutoEnableStandards value: {data!r}")
    return cast(AutoEnableStandards, data)
