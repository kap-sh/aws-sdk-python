"""Generated from Smithy shape ``com.amazonaws.iot#EffectivePolicies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.effective_policy

EffectivePolicies: TypeAlias = list["capo_iot.types.effective_policy.EffectivePolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: EffectivePolicies) -> list:
    import capo_iot.types.effective_policy

    out: list = []
    for item in value:
        out.append(capo_iot.types.effective_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> EffectivePolicies:
    import capo_iot.types.effective_policy

    out: EffectivePolicies = []
    for item in data:
        out.append(capo_iot.types.effective_policy.deserialize_json(item))
    return out
