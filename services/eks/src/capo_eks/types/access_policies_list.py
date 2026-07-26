"""Generated from Smithy shape ``com.amazonaws.eks#AccessPoliciesList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.access_policy

AccessPoliciesList: TypeAlias = list["capo_eks.types.access_policy.AccessPolicy"]


# --- restJson1 ser/de ---
def serialize_json(value: AccessPoliciesList) -> list:
    import capo_eks.types.access_policy

    out: list = []
    for item in value:
        out.append(capo_eks.types.access_policy.serialize_json(item))
    return out


def deserialize_json(data: list) -> AccessPoliciesList:
    import capo_eks.types.access_policy

    out: AccessPoliciesList = []
    for item in data:
        out.append(capo_eks.types.access_policy.deserialize_json(item))
    return out
