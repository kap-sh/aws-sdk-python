"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_policy_version

CoreNetworkPolicyVersionList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_policy_version.CoreNetworkPolicyVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyVersionList) -> list:
    import aws_sdk_networkmanager.types.core_network_policy_version

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_policy_version.serialize_json(
                item
            )
        )
    return out


def deserialize_json(data: list) -> CoreNetworkPolicyVersionList:
    import aws_sdk_networkmanager.types.core_network_policy_version

    out: CoreNetworkPolicyVersionList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_policy_version.deserialize_json(
                item
            )
        )
    return out
