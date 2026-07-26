"""Generated from Smithy shape ``com.amazonaws.efs#LifecyclePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_efs.types.lifecycle_policy

LifecyclePolicies: TypeAlias = list["capo_efs.types.lifecycle_policy.LifecyclePolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: LifecyclePolicies) -> list:
    import capo_efs.types.lifecycle_policy

    out: list = []
    for item in value:
        out.append(capo_efs.types.lifecycle_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> LifecyclePolicies:
    import capo_efs.types.lifecycle_policy

    out: LifecyclePolicies = []
    for item in data:
        out.append(capo_efs.types.lifecycle_policy.deserialize_json(item))
    return out
