"""Generated from Smithy shape ``com.amazonaws.ec2#DeviceTrustProviderTypeList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_ec2.types.device_trust_provider_type

DeviceTrustProviderTypeList: TypeAlias = list[
    "aws_sdk_ec2.types.device_trust_provider_type.DeviceTrustProviderType"
]
