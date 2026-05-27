"""Generated from Smithy shape ``com.amazonaws.eks#AddonPodIdentityConfigurationList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.addon_pod_identity_configuration

AddonPodIdentityConfigurationList: TypeAlias = list[
    "aws_sdk_eks.types.addon_pod_identity_configuration.AddonPodIdentityConfiguration"
]


# --- restJson1 ser/de ---
def serialize_json(value: AddonPodIdentityConfigurationList) -> list:
    import aws_sdk_eks.types.addon_pod_identity_configuration

    out: list = []
    for item in value:
        out.append(
            aws_sdk_eks.types.addon_pod_identity_configuration.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> AddonPodIdentityConfigurationList:
    import aws_sdk_eks.types.addon_pod_identity_configuration

    out: AddonPodIdentityConfigurationList = []
    for item in data:
        out.append(
            aws_sdk_eks.types.addon_pod_identity_configuration.deserialize_json(item)
        )
    return out
