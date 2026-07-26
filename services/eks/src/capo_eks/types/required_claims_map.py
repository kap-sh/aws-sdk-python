"""Generated from Smithy shape ``com.amazonaws.eks#requiredClaimsMap``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.required_claims_key
    import capo_eks.types.required_claims_value

requiredClaimsMap: TypeAlias = dict[
    "capo_eks.types.required_claims_key.requiredClaimsKey",
    "capo_eks.types.required_claims_value.requiredClaimsValue",
]


# --- restJson1 ser/de ---
def serialize_json(input_to_serialize: requiredClaimsMap) -> dict:
    out: dict = {}
    for key, value in input_to_serialize.items():
        out[key] = value
    return out


def deserialize_json(data: dict) -> requiredClaimsMap:
    out: requiredClaimsMap = {}
    for key, value in data.items():
        out[key] = value
    return out
