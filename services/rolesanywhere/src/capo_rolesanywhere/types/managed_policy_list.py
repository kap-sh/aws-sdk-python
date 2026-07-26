"""Generated from Smithy shape ``com.amazonaws.rolesanywhere#ManagedPolicyList``."""

from typing import TypeAlias

ManagedPolicyList: TypeAlias = list["str"]


# --- restJson1 ser/de ---
def serialize_json(value: ManagedPolicyList) -> list:
    return list(value)


def deserialize_json(data: list) -> ManagedPolicyList:
    return list(data)
