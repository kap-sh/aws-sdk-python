"""Generated from Smithy shape ``com.amazonaws.eks#AddonPodIdentityAssociationsList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.addon_pod_identity_associations

AddonPodIdentityAssociationsList: TypeAlias = list[
    "capo_eks.types.addon_pod_identity_associations.AddonPodIdentityAssociations"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonPodIdentityAssociationsList) -> list:
    import capo_eks.types.addon_pod_identity_associations

    out: list = []
    for item in value:
        out.append(capo_eks.types.addon_pod_identity_associations.serialize_json(item))
    return out


def deserialize_json(data: list) -> AddonPodIdentityAssociationsList:
    import capo_eks.types.addon_pod_identity_associations

    out: AddonPodIdentityAssociationsList = []
    for item in data:
        out.append(
            capo_eks.types.addon_pod_identity_associations.deserialize_json(item)
        )
    return out
