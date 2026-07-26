"""Generated from Smithy shape ``com.amazonaws.sesv2#PolicyMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_sesv2.types.policy
    import capo_sesv2.types.policy_name

PolicyMap: TypeAlias = dict[
    "capo_sesv2.types.policy_name.PolicyName", "capo_sesv2.types.policy.Policy"
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: PolicyMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> PolicyMap:
    out: PolicyMap = {}
    for key, value in data.items():
        out[key] = value
    return out
