"""Generated from Smithy shape ``com.amazonaws.networkmanager#CoreNetworkPolicyErrorList``."""

from typing import TYPE_CHECKING, TypeAlias

if TYPE_CHECKING:
    import aws_sdk_networkmanager.types.core_network_policy_error

CoreNetworkPolicyErrorList: TypeAlias = list[
    "aws_sdk_networkmanager.types.core_network_policy_error.CoreNetworkPolicyError"
]


# --- restJson1 ser/de ---
def serialize_json(value: CoreNetworkPolicyErrorList) -> list:
    import aws_sdk_networkmanager.types.core_network_policy_error

    out: list = []
    for item in value:
        out.append(
            aws_sdk_networkmanager.types.core_network_policy_error.serialize_json(item)
        )
    return out


def deserialize_json(data: list) -> CoreNetworkPolicyErrorList:
    import aws_sdk_networkmanager.types.core_network_policy_error

    out: CoreNetworkPolicyErrorList = []
    for item in data:
        out.append(
            aws_sdk_networkmanager.types.core_network_policy_error.deserialize_json(
                item
            )
        )
    return out
