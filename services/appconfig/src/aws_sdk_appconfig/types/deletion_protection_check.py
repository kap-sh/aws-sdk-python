"""Generated from Smithy shape ``com.amazonaws.appconfig#DeletionProtectionCheck``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_appconfig.errors import DeserializationError

DeletionProtectionCheck: TypeAlias = Literal[
    "ACCOUNT_DEFAULT",
    "APPLY",
    "BYPASS",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "ACCOUNT_DEFAULT",
        "APPLY",
        "BYPASS",
    )
)


def serialize_json(value: DeletionProtectionCheck) -> str:
    return value


def deserialize_json(data: str) -> DeletionProtectionCheck:
    if data not in _VALUES:
        raise DeserializationError(f"unknown DeletionProtectionCheck value: {data!r}")
    return cast(DeletionProtectionCheck, data)
