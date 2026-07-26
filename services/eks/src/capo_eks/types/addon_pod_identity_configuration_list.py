"""Generated from Smithy shape ``com.amazonaws.eks#AddonPodIdentityConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_eks.types.addon_pod_identity_configuration

AddonPodIdentityConfigurationList: TypeAlias = list[
    "capo_eks.types.addon_pod_identity_configuration.AddonPodIdentityConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonPodIdentityConfigurationList) -> list:
    import capo_eks.types.addon_pod_identity_configuration

    out: list = []
    for item in value:
        out.append(capo_eks.types.addon_pod_identity_configuration.serialize_json(item))
    return out


def deserialize_json(data: list) -> AddonPodIdentityConfigurationList:
    import capo_eks.types.addon_pod_identity_configuration

    out: AddonPodIdentityConfigurationList = []
    for item in data:
        out.append(
            capo_eks.types.addon_pod_identity_configuration.deserialize_json(item)
        )
    return out
