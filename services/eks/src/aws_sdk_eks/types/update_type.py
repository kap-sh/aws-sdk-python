"""Generated from Smithy shape ``com.amazonaws.eks#UpdateType``."""

from typing import Literal, TypeAlias, cast

from aws_sdk_eks.errors import DeserializationError

UpdateType: TypeAlias = Literal[
    "VersionUpdate",
    "EndpointAccessUpdate",
    "LoggingUpdate",
    "ConfigUpdate",
    "AssociateIdentityProviderConfig",
    "DisassociateIdentityProviderConfig",
    "AssociateEncryptionConfig",
    "AddonUpdate",
    "VpcConfigUpdate",
    "AccessConfigUpdate",
    "UpgradePolicyUpdate",
    "ZonalShiftConfigUpdate",
    "AutoModeUpdate",
    "RemoteNetworkConfigUpdate",
    "DeletionProtectionUpdate",
    "ControlPlaneScalingConfigUpdate",
    "VendedLogsUpdate",
]


# --- restJson1 ser/de ---
_VALUES: frozenset[str] = frozenset(
    (
        "VersionUpdate",
        "EndpointAccessUpdate",
        "LoggingUpdate",
        "ConfigUpdate",
        "AssociateIdentityProviderConfig",
        "DisassociateIdentityProviderConfig",
        "AssociateEncryptionConfig",
        "AddonUpdate",
        "VpcConfigUpdate",
        "AccessConfigUpdate",
        "UpgradePolicyUpdate",
        "ZonalShiftConfigUpdate",
        "AutoModeUpdate",
        "RemoteNetworkConfigUpdate",
        "DeletionProtectionUpdate",
        "ControlPlaneScalingConfigUpdate",
        "VendedLogsUpdate",
    )
)


def serialize_json(value: UpdateType) -> str:
    return value


def deserialize_json(data: str) -> UpdateType:
    if data not in _VALUES:
        raise DeserializationError(f"unknown UpdateType value: {data!r}")
    return cast(UpdateType, data)
