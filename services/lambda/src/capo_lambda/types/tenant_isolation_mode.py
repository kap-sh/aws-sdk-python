"""Generated from Smithy shape ``com.amazonaws.lambda#TenantIsolationMode``."""

from typing import Literal, TypeAlias, cast

TenantIsolationMode: TypeAlias = Literal["PER_TENANT",]


# --- restJson1 ser/de ---
def serialize_json(value: TenantIsolationMode) -> str:
    return value


def deserialize_json(data: str) -> TenantIsolationMode:
    return cast(TenantIsolationMode, data)
