"""Generated from Smithy shape ``com.amazonaws.eks#UpdateType``."""

from typing import Literal, TypeAlias, cast

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
def serialize_json(value: UpdateType) -> str:
    return value


def deserialize_json(data: str) -> UpdateType:
    return cast(UpdateType, data)
