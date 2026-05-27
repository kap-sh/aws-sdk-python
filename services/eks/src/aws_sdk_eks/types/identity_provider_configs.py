"""Generated from Smithy shape ``com.amazonaws.eks#IdentityProviderConfigs``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_eks.types.identity_provider_config

IdentityProviderConfigs: TypeAlias = list[
    "aws_sdk_eks.types.identity_provider_config.IdentityProviderConfig"
]


# --- restJson1 ser/de ---
def serialize_json(value: IdentityProviderConfigs) -> list:
    import aws_sdk_eks.types.identity_provider_config

    out: list = []
    for item in value:
        out.append(aws_sdk_eks.types.identity_provider_config.serialize_json(item))
    return out


def deserialize_json(data: list) -> IdentityProviderConfigs:
    import aws_sdk_eks.types.identity_provider_config

    out: IdentityProviderConfigs = []
    for item in data:
        out.append(aws_sdk_eks.types.identity_provider_config.deserialize_json(item))
    return out
