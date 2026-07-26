"""Generated from Smithy shape ``com.amazonaws.eks#PodIdentityAssociationSummaries``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.pod_identity_association_summary

PodIdentityAssociationSummaries: TypeAlias = list[
    "capo_eks.types.pod_identity_association_summary.PodIdentityAssociationSummary"
]


# --- restJson1 ser/de ---
def serialize_json(value: PodIdentityAssociationSummaries) -> list:
    import capo_eks.types.pod_identity_association_summary

    out: list = []
    for item in value:
        out.append(capo_eks.types.pod_identity_association_summary.serialize_json(item))
    return out


def deserialize_json(data: list) -> PodIdentityAssociationSummaries:
    import capo_eks.types.pod_identity_association_summary

    out: PodIdentityAssociationSummaries = []
    for item in data:
        out.append(
            capo_eks.types.pod_identity_association_summary.deserialize_json(item)
        )
    return out
