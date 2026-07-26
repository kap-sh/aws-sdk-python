"""Generated from Smithy shape ``com.amazonaws.iot#PolicyNames``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.policy_name

PolicyNames: TypeAlias = list["capo_iot.types.policy_name.PolicyName"]


# --- restJson1 ser/de ---
def serialize_json(value: PolicyNames) -> list:
    return list(value)


def deserialize_json(data: list) -> PolicyNames:
    return list(data)
