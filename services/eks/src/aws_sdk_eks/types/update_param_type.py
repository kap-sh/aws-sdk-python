"""Generated from Smithy shape ``com.amazonaws.eks#UpdateParamType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

UpdateParamType: TypeAlias = Literal[
    "Version",
    "PlatformVersion",
    "EndpointPrivateAccess",
    "EndpointPublicAccess",
    "ClusterLogging",
    "DesiredSize",
    "LabelsToAdd",
    "LabelsToRemove",
    "TaintsToAdd",
    "TaintsToRemove",
    "MaxSize",
    "MinSize",
    "ReleaseVersion",
    "PublicAccessCidrs",
    "LaunchTemplateName",
    "LaunchTemplateVersion",
    "IdentityProviderConfig",
    "EncryptionConfig",
    "AddonVersion",
    "ServiceAccountRoleArn",
    "ResolveConflicts",
    "MaxUnavailable",
    "MaxUnavailablePercentage",
    "NodeRepairEnabled",
    "UpdateStrategy",
    "ConfigurationValues",
    "SecurityGroups",
    "Subnets",
    "AuthenticationMode",
    "PodIdentityAssociations",
    "UpgradePolicy",
    "ZonalShiftConfig",
    "ComputeConfig",
    "StorageConfig",
    "KubernetesNetworkConfig",
    "RemoteNetworkConfig",
    "DeletionProtection",
    "NodeRepairConfig",
    "VendedLogs",
    "UpdatedTier",
    "PreviousTier",
    "WarmPoolEnabled",
    "WarmPoolMaxGroupPreparedCapacity",
    "WarmPoolMinSize",
    "WarmPoolState",
    "WarmPoolReuseOnScaleIn",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "Version",
        "PlatformVersion",
        "EndpointPrivateAccess",
        "EndpointPublicAccess",
        "ClusterLogging",
        "DesiredSize",
        "LabelsToAdd",
        "LabelsToRemove",
        "TaintsToAdd",
        "TaintsToRemove",
        "MaxSize",
        "MinSize",
        "ReleaseVersion",
        "PublicAccessCidrs",
        "LaunchTemplateName",
        "LaunchTemplateVersion",
        "IdentityProviderConfig",
        "EncryptionConfig",
        "AddonVersion",
        "ServiceAccountRoleArn",
        "ResolveConflicts",
        "MaxUnavailable",
        "MaxUnavailablePercentage",
        "NodeRepairEnabled",
        "UpdateStrategy",
        "ConfigurationValues",
        "SecurityGroups",
        "Subnets",
        "AuthenticationMode",
        "PodIdentityAssociations",
        "UpgradePolicy",
        "ZonalShiftConfig",
        "ComputeConfig",
        "StorageConfig",
        "KubernetesNetworkConfig",
        "RemoteNetworkConfig",
        "DeletionProtection",
        "NodeRepairConfig",
        "VendedLogs",
        "UpdatedTier",
        "PreviousTier",
        "WarmPoolEnabled",
        "WarmPoolMaxGroupPreparedCapacity",
        "WarmPoolMinSize",
        "WarmPoolState",
        "WarmPoolReuseOnScaleIn",
    )
)


def serialize_json(value: UpdateParamType) -> str:
    return value


def deserialize_json(data: str) -> UpdateParamType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateParamType value: {data!r}")
    return cast(UpdateParamType, data)
