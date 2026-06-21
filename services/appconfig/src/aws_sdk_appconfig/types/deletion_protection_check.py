"""Generated from Smithy shape ``com.amazonaws.appconfig#DeletionProtectionCheck``."""

from typing import Literal, TypeAlias, cast

DeletionProtectionCheck: TypeAlias = Literal[
    "ACCOUNT_DEFAULT",
    "APPLY",
    "BYPASS",
]


# --- restJson1 ser/de ---
def serialize_json(value: DeletionProtectionCheck) -> str:
    return value


def deserialize_json(data: str) -> DeletionProtectionCheck:
    return cast(DeletionProtectionCheck, data)
