"""Generated from Smithy shape ``com.amazonaws.mpa#Policies``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_mpa.types.policy

Policies: TypeAlias = list["capo_mpa.types.policy.Policy"]


# --- restJson1 ser/de ---
def serialize_json(value: Policies) -> list:
    import capo_mpa.types.policy

    out: list = []
    for item in value:
        out.append(capo_mpa.types.policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> Policies:
    import capo_mpa.types.policy

    out: Policies = []
    for item in data:
        out.append(capo_mpa.types.policy.deserialize_json(item))
    return out
