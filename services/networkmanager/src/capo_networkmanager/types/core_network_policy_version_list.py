"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyVersionList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import capo_networkmanager.types.core_network_policy_version

CoreNetworkPolicyVersionList: TypeAlias = list[
    "capo_networkmanager.types.core_network_policy_version.CoreNetworkPolicyVersion"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyVersionList) -> list:
    import capo_networkmanager.types.core_network_policy_version

    out: list = []
    for item in value:
        out.append(
            capo_networkmanager.types.core_network_policy_version.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkPolicyVersionList:
    import capo_networkmanager.types.core_network_policy_version

    out: CoreNetworkPolicyVersionList = []
    for item in data:
        out.append(
            capo_networkmanager.types.core_network_policy_version.deserialize_json(item)
        )
    return out
