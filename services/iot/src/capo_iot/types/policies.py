"""Generated from Smithy shape ``com.amazonaws.iot#Policies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_iot.types.policy

Policies: TypeAlias = list["capo_iot.types.policy.Policy"]


# --- restJson1 ser/de ---
def serialize_json(value: Policies) -> list:
    import capo_iot.types.policy

    out: list = []
    for item in value:
        out.append(capo_iot.types.policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Policies:
    import capo_iot.types.policy

    out: Policies = []
    for item in data:
        out.append(capo_iot.types.policy.deserialize_json(item))
    return out
