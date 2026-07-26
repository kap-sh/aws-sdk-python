"""Generated from Smithy shape ``com.amazonaws.connecthealth#ProviderRole``."""

from typing import Literal, TypeAlias, cast

ProviderRole: TypeAlias = Literal["CLINICIAN",]


# --- restJson1 ser/de ---
def serialize_json(value: ProviderRole) -> str:
    return value


def deserialize_json(data: str) -> ProviderRole:
    return cast(ProviderRole, data)
