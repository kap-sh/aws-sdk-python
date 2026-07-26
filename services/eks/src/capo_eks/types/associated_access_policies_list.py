"""Generated from Smithy shape ``com.amazonaws.eks#AssociatedAccessPoliciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.associated_access_policy

AssociatedAccessPoliciesList: TypeAlias = list[
    "capo_eks.types.associated_access_policy.AssociatedAccessPolicy"
]


# --- restJson1 ser/de ---
def serialize_json(value: AssociatedAccessPoliciesList) -> list:
    import capo_eks.types.associated_access_policy

    out: list = []
    for item in value:
        out.append(capo_eks.types.associated_access_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AssociatedAccessPoliciesList:
    import capo_eks.types.associated_access_policy

    out: AssociatedAccessPoliciesList = []
    for item in data:
        out.append(capo_eks.types.associated_access_policy.deserialize_json(item))
    return out
